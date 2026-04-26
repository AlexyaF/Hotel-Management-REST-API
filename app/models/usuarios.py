from app.sql_alchemy import banco
from flask import request, url_for
from requests import post

mailgun_domain ='teste'
maingun_api_key = 'teste-e3c0807f-2073d3f7'
from_title = 'NO-REPLY'
from_email = 'no-reply@restapi.com'

class UserModel(banco.Model): #recebe todas as tabelas do banco
    __tablename__ = 'usuarios' #filtra pelo nome

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40),nullable=False, unique=True)
    email = banco.Column(banco.String(40), nullable=False, unique=True)
    senha = banco.Column(banco.String(40))
    ativado = banco.Column(banco.Boolean, default=True)

    def __init__(self, login,senha,email,ativado):
        self.login = login
        self.senha = senha
        self.email = email
        self.ativado = ativado

    def json(self):
     return {
          'user_id': self.user_id,
          'login':self.login,
          'ativado':self.ativado
     }
    
    def send_confirmation_email(self):
         #tirar a barra final da url
        link = request.url_root[:-1] + url_for('userconfirm', user_id=self.user_id)
        return post('https://api.mailgun.net/v3/{}/messages'.format(mailgun_domain), 
                    auth=('api', maingun_api_key), 
                    data={
                        'from':'{} <{}>'.format(from_title, from_email), 
                        'to':self.email, 
                        'subject':'Confirmation', 
                        'text':'Clique no link para confirmar seu cadastro: {}'.format(link),
                        'html':'<html><p> Confirme seu cadastro clicando no link a seguir: <a href="{}">CONFIRMAR EMAIL</a></p></html>'.format(link)
                        }
                    )

    @classmethod
    def find_user(cls, user_id): #cls para a função receber a propria classe
        user = cls.query.filter_by(user_id=user_id).first() # select * from usuarios where user_id=user_id
        if user:
            return user
        else:
            return None

    @classmethod  
    def find_by_login(cls,login):
        user = cls.query.filter_by(login=login).first() # select * from usuarios where login=login)
        if user:
            return user
        else:
            return None

    @classmethod  
    def find_by_email(cls,email):
        user = cls.query.filter_by(email=email).first() # select * from usuarios where email=email
        if user:
            return user
        else:
            return None
            
    def save_user(self):
        banco.session.add(self) #Abre uma sessão com o banco e adiciona o objeto
        banco.session.commit()

    def deleted_user(self):
        banco.session.delete(self)
        banco.session.commit()


