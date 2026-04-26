from app.sql_alchemy import banco


class HotelModel(banco.Model): #recebe todas as tabelas do banco
    __tablename__ = 'hoteis' #filtra pelo nome

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    valor_diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(80))
    site_id = banco.Column(banco.Integer, banco.ForeignKey('sites.site_id'))

    def __init__(self, nome, estrelas,valor_diaria,cidade, site_id):
        self.nome = nome
        self.estrelas = estrelas
        self.valor_diaria = valor_diaria
        self.cidade = cidade
        self.site_id = site_id

    def json(self):
     return {
          'id': self.id,
          'nome':self.nome,
          'estrelas':self.estrelas,
          'valor_diaria':self.valor_diaria,
          'cidade':self.cidade,
          'site_id':self.site_id
     }
    
    @classmethod
    def findHotel(cls, hotel_id): #cls para a função receber a propria classe
        hotel = cls.query.filter_by(id=hotel_id).first() # select * from hoteis where id = hotel_id
        if hotel:
            return hotel
        else:
            return None
        
    def save_hotel(self):
        banco.session.add(self) #Abre uma sessão com o banco e adiciona o objeto
        banco.session.commit()

    def update_hotel(self, nome, estrelas, valor_diaria, cidade, site_id):
        self.nome = nome
        self.estrelas = estrelas
        self.valor_diaria = valor_diaria
        self.cidade = cidade
        self.site_id = site_id

    def deleted_hotel(self):
        banco.session.delete(self)
        banco.session.commit()