from flask_restful import Resource, reqparse
from models.usuarios import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
from blacklist import BLACKLIST
import traceback
from flask import make_response, render_template


argumentos = reqparse.RequestParser()
argumentos.add_argument('login', type=str, required=True, help="The field 'login' can't be empty") #tipo de dado qu vai ceitar, se é obrigatório, descrição caso valor informado incorreto
argumentos.add_argument('senha',type=str, required=True, help="The field 'senha' can't be empty")
argumentos.add_argument('email',type=str, required=True, help="The field 'email' can't be empty")
argumentos.add_argument('ativado',type=bool)


argumentos_login = reqparse.RequestParser()
argumentos_login.add_argument('login', type=str, required=True, help="The field 'login' can't be empty") #tipo de dado qu vai ceitar, se é obrigatório, descrição caso valor informado incorreto
argumentos_login.add_argument('senha',type=str, required=True, help="The field 'senha' can't be empty")

class User(Resource):
    #Buscar
    jwt_required()    
    def get(self, user_id):
       user =  UserModel.find_user(user_id)
       if user is not None:
            return user.json(), 200
       return {'error_message': 'Error, id not found'}, 404
        

    #Deletar
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user is not None:
                try:
                    user.deleted_user()
                except Exception as e:
                    return{'message': f'An internal error ocurred trying to delete user:{e}'}, 500
                
                return {'Deleted':user.json()}, 200
        return {'error_message': 'Error, id not found'}, 404


#Criar
class newUser(Resource):
    #cadastro
    def post(self):
        dados = argumentos.parse_args()
        if not dados.get('email') or dados.get('email') is None:
            return {"message":"The filed email canoot be left blank"},400
        
        if UserModel.find_by_email(dados['email']):
            return {"message": "the email '{}' already exists".format(dados['login'])}, 400
        
        if UserModel.find_by_login(dados['login']):
            return {"message": "the login '{}' already exists".format(dados['login'])}
        
        user = UserModel(**dados) #cria um objeto
        user.ativado = False
        try:
            user.save_user()
            user.send_confirmation_email()
            return {"message": "User created sucessfully!"},201
        except Exception as e:
            user.deleted_user()
            traceback.print_exc()
            return{"message": f"An internal error ocurred trying to save user:{e}"}, 500
        

class userLogin(Resource):
    @classmethod
    def post(cls):
        dados = argumentos_login.parse_args()
        user = UserModel.find_by_login(dados['login'])

        if user and hmac.compare_digest(user.senha, dados['senha']):
            if user.ativado:
                token_de_acesso = create_access_token(identity=str(user.user_id))
                return {'access_token': token_de_acesso}, 200
            else:
                return {'message':'Email confirmation required'}, 400
        return {'message':'The username or password is incorrect'}, 401
    
class userLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT Token Identifier 
        BLACKLIST.add(jwt_id)
        return {'message':'Logged out sucessfully!'},200
    

    
class userConfirm(Resource):
    #raiz_do_site/confirmacao/{user_id}
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_user(user_id)

        if not user:
            return{"message": "User id '{}' not found."}, 404
        
        user.ativado = True
        user.save_user()
        # return {'message':'User saved sucessfully!'},200
        #pg HTML
        headers = {'Content-Type':'txt/html'}
        return make_response(render_template('user_confirm.html', email=user.email, usuario=user.login),200, headers)