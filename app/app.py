from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel, newHotel
from models.hotel import HotelModel
from resources.usuario import User, newUser, userLogin, userLogout, userConfirm
from models.usuarios import UserModel
from resources.site import Site, Sites
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLE'] = True
api = Api(app)
jwt = JWTManager(app)

@app.before_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_invalido(jwt_header, jwt_payload):
    return {'message': 'You have been logged out'}, 401 

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<int:hotel_id>')
api.add_resource(newHotel, '/hoteis/new')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(newUser, '/usuarios/new')
api.add_resource(userLogin, '/usuarios/login')
api.add_resource(userLogout, '/usuarios/logout')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/sites/<string:url>')
api.add_resource(userConfirm, '/confirmacao/<int:user_id>')

if __name__ == '__main__':
    from app.sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)