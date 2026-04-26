import sqlite3
from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from models.site import SiteModel
from app.sql_alchemy import banco
from resources.filtros import normalize_path_params, consult_no_city, consult_city
from sqlalchemy import text
from flask_jwt_extended import jwt_required

path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

#Buscar geral
class Hoteis(Resource):
    # @jwt_required()
    def get(self):
        dados = dict(path_params.parse_args())
        dados_validos = {chave: dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos) #me retorna um dicionario  
        if not parametros.get('cidade'):  #Caso valor nao exista o codigo nao quebra
            # print(text(consult_no_city), parametros)
            resultado = banco.session.execute(text(consult_no_city), parametros)
        else:
            # print(text(consult_city), parametros)
            resultado = banco.session.execute(text(consult_city), parametros)
            
        hoteis = []
        for line in resultado:
            hoteis.append({
                'id': line[0],
                'nome':line[1],
                'estrelas':line[2],
                'valor_diaria':line[3],
                'cidade':line[4],
                'site_id':line[5]
            })

        return hoteis, 200
        # return {'Hoteis': [hotel.json() for hotel in HotelModel.query.all()]} # se fosse para retornar todos hoteis sem nenhum filtro, inclusive sem filtro default


#Criar
class newHotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' can't be empty") #tipo de dado qu vai ceitar, e se é obrigatório, descrição caso valor informado incorreto
    argumentos.add_argument('estrelas', type=float)
    argumentos.add_argument('valor_diaria', type=float, help="The value can't be a string")
    argumentos.add_argument('cidade', type=str)
    argumentos.add_argument('site_id', type=int, required=True, help="Every hotel need a site")


    @jwt_required()
    def post(self):
        dados = newHotel.argumentos.parse_args()
        hotel = HotelModel(**dados) #cria um objeto

        if not SiteModel.find_site_by_id(dados.get('site_id')):
            return {'message':'The hotel must be associated to a valid site id'},400

        try:
            hotel.save_hotel()
        except Exception as e:
            return{'message': f'An internal error ocurred trying to save hotel:{e}'}, 500
        
        return hotel.json(), 201


class Hotel(Resource):
    #Buscar  
    @jwt_required()       
    def get(self, hotel_id):
       hotel =  HotelModel.findHotel(hotel_id)
       if hotel is not None:
            return hotel.json(), 200
       return {'error_message': 'Error, id not found'}, 404
        

    #Alterar/Criar  
    @jwt_required() 
    def put(self, hotel_id):
        from models.hotel import HotelModel
        dados = newHotel.argumentos.parse_args()
        hotel_encontrado =  HotelModel.findHotel(hotel_id)

        if hotel_encontrado is not None:
            hotel_encontrado.update_hotel(**dados) #altera hotel existente
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        else:
            novo_hotel = HotelModel(**dados)
            try:
                novo_hotel.save_hotel()
            except Exception as e:
                return{'message': f'An internal error ocurred trying to save hotel:{e}'}, 500
            
            return novo_hotel.json(), 201 #success created


    #Deletar
    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.findHotel(hotel_id)
        if hotel is not None:
                try:
                    hotel.deleted_hotel()
                except Exception as e:
                    return{'message': f'An internal error ocurred trying to delete hotel:{e}'}, 500
                
                return {'Deleted':hotel.json()}, 200
        return {'error_message': 'Error, id not found'}, 404
