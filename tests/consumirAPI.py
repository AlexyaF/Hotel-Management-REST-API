import requests

url = ''

def get_hoteis():
    #HOTEIS
    params = {
        'cidade':'Fortaleza'
        #demais filtros de pesquisa
    }
    endpoint_hotel = url + '/hoteis'
    response = requests.get(endpoint_hotel, json=[], params=params)
    hoteis = response.json()
    print(hoteis)

def cadastrar():
    #CADASTRO
    endpoint_cadastro = url + '/usuarios/new'
    body={
        'login':'Alexya',
        'senha':'123456'
    }
    response = requests.post(endpoint_cadastro, headers={'Content-Type':'application/json'},json=body)
    print(response.json())

def login():
    #LOGIN
    endpoint_login = url + '/usuarios/login'
    body={
        'login':'Alexya',
        'senha':'123456'
    }
    response = requests.post(endpoint_login, headers={'Content-Type':'application/json'},json=body)
    token_json = response.json()
    token = token_json['access_token']
    print(f'TOKEN:{token}')
    return token

def criar_hotel():
    token = login()
    endpoint_postHotel = url + '/hoteis/new'
    header = {
        'Authorization':f'Bearer {token}'
    }
    body = {
        "nome": "Hotel teste python",
        "estrelas": 4.5,
        "valor_diaria": 452.00,
        "cidade": "Rio de Janeiro",
        "site_id":1
    }

    response = requests.post(endpoint_postHotel, headers=header, json=body)
    print(response.json())

def alterar_hotel():
    token = login()
    endpoint_postHotel = url + '/hoteis/11'
    header = {
        'Authorization':f'Bearer {token}'
    }
    body = {
        "nome": "Hotel alterado python",
        "estrelas": 4.5,
        "valor_diaria": 452.00,
        "cidade": "Rio de Janeiro",
        "site_id":1
    }

    response = requests.put(endpoint_postHotel, headers=header, json=body)
    print(response.status_code)
    print(response.json())

def delete_hotel():
    token = login()
    endpoint_postHotel = url + '/hoteis/11'
    header = {
        'Authorization':f'Bearer {token}'
    }
    response = requests.delete(endpoint_postHotel, headers=header)
    print(response.status_code)
    print(response.json())

def get_user(id):
    token = login()
    endpoint_user_id = url + f'/usuarios/{id}'
    header = {
        'Authorization':f'Bearer {token}'
    }
    response = requests.get(endpoint_user_id, headers=header)
    print(response.json())

def delete_user(id):
    token = login()
    endpoint_user_id = url + f'/usuarios/{id}'
    header = {
        'Authorization':f'Bearer {token}'
    }
    response = requests.delete(endpoint_user_id, headers=header)
    print(response.json())
