from app.sql_alchemy import banco


class SiteModel(banco.Model): #recebe todas as tabelas do banco
    __tablename__ = 'sites' #filtra pelo nome

    site_id = banco.Column(banco.Integer, primary_key=True)
    url = banco.Column(banco.String(80))
    hoteis = banco.relationship('HotelModel') #lista de objetos hoteis


    def __init__(self, url):
        self.url = url

    def json(self):
     return {
          'site_id': self.site_id,
          'url':self.url,
          'hoteis' : [hotel.json() for hotel in self.hoteis]
     }
    
    @classmethod
    def find_site(cls, url): #cls para a função receber a propria classe
        site = cls.query.filter_by(url=url).first() 
        if site:
            return site
        else:
            return None
        
    @classmethod
    def find_site_by_id(cls, site_id): #cls para a função receber a propria classe
        site = cls.query.filter_by(site_id=site_id).first() 
        if site:
            return site
        else:
            return None
        

        
    def save_site(self):
        banco.session.add(self) #Abre uma sessão com o banco e adiciona o objeto
        banco.session.commit()

    def deleted_site(self):
        #deletando hoteis associados ao site
        [hotel.deleted_hotel() for hotel in self.hoteis]
        banco.session.delete(self)
        banco.session.commit()