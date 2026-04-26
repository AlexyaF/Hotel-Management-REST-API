# 🏨 Hotel Management REST API

🇺🇸 English version below  
🇧🇷 Versão em português abaixo


## 🇺🇸 English

## ▶️ How to run
pip install -r requirements.txt  
python app.py

--- 

This project is a REST API built with Flask that allows users to manage hotels, users, and booking platforms (sites).  

It simulates a real-world backend service, including authentication, data validation, and full CRUD operations, focusing on structured data handling and secure access control.

---

## 🎯 Purpose

The goal of this API is to simulate a production-ready backend system responsible for managing hotel data across different platforms.  

It includes features such as user authentication, email confirmation, protected endpoints, and relational data management between hotels and sites.

---

## 🚀 Features

- Full CRUD operations for:
  - Hotels
  - Users
  - Sites (platforms)
- User authentication (login/logout)
- Token-based authorization (protected routes)
- Email confirmation requirement for login
- Advanced filtering for hotel search
- Relational data validation (hotel must belong to a site)
- Error handling with proper HTTP status codes

---

## ⚙️ Tech Stack

- Python
- Flask
- REST API
- SQL (relational database)
- JWT Authentication

---

## 🔐 Authentication

Some endpoints require authentication using a Bearer Token:


Authorization: Bearer {access_token}


Token is obtained via login.

---

## 🔎 Endpoints Overview

### 🏨 Hotels

#### Get all hotels (with filters)

GET /hoteis?cidade=&estrelas_min=&estrelas_max=&diaria_min=&diaria_max=&limit=&offset=


#### Get hotel by ID

GET /hoteis/{id}


#### Create hotel (auth required)

POST /hoteis/new


#### Update hotel (auth required)

PUT /hoteis/{id}


#### Delete hotel (auth required)

DELETE /hoteis/{id}


---

### 👤 Users

#### Register user

POST /usuarios/new


#### Login

POST /usuarios/login


#### Logout (auth required)

POST /usuarios/logout


#### Get user data

GET /usuarios/{id}


#### Delete user (auth required)

DELETE /usuarios/{id}


---

### 🌐 Sites

#### Create site (auth required)

POST /sites/{url}


#### Get all sites

GET /sites


#### Get site by URL

GET /sites/{url}


#### Delete site (auth required)

DELETE /sites/{url}


---

## 🔍 Example Request

### Create Hotel

```json
POST /hoteis/new
{
  "id": 1,
  "nome": "Inga Hotel",
  "estrelas": 3.5,
  "valor_diaria": 250.9,
  "cidade": "Maringá",
  "site_id": 1
}
📦 Example Response
{
  "id": 1,
  "nome": "Inga Hotel",
  "estrelas": 3.5,
  "valor_diaria": 250.9,
  "cidade": "Maringá",
  "site_id": 1
}
```
---
### ⚠️ Error Handling

The API returns appropriate HTTP status codes:

- 200 OK → Success
- 201 Created → Resource created
- 400 Bad Request → Invalid input
- 401 Unauthorized → Missing/invalid token
- 404 Not Found → Resource not found

### 🧠 Key Concepts Demonstrated
- RESTful API design
- Backend architecture simulation
- Authentication and authorization
- Data validation and relational integrity
- Query filtering and pagination
- Error handling and API reliability

### 📌 Notes
- Hotels must be associated with a valid site
- Users must confirm email before login
- Protected routes require authentication token

### 💡 Future Improvements
- API documentation with Swagger / OpenAPI
- Docker containerization
- Deployment with CI/CD pipeline
- Rate limiting and logging

### 📎 Author
Developed as a backend API project to simulate real-world data processing and service architecture.

--- 
## 🇧🇷 Português

Este projeto é uma API REST desenvolvida com Flask que permite gerenciar hotéis, usuários e plataformas (sites).  

A aplicação simula um serviço backend real, incluindo autenticação, validação de dados e operações completas de CRUD, com foco em manipulação estruturada de dados e controle de acesso seguro.

---

## 🎯 Objetivo

O objetivo desta API é simular um sistema backend de produção responsável por gerenciar dados de hotéis em diferentes plataformas.  

O projeto inclui funcionalidades como autenticação de usuários, confirmação de e-mail, rotas protegidas e gerenciamento de dados relacionais entre hotéis e sites.

---

## 🚀 Funcionalidades

- Operações completas de CRUD para:
  - Hotéis
  - Usuários
  - Sites (plataformas)
- Autenticação de usuários (login/logout)
- Autorização via token (rotas protegidas)
- Necessidade de confirmação de e-mail para login
- Filtros avançados para busca de hotéis
- Validação de dados relacionais (hotel deve estar vinculado a um site)
- Tratamento de erros com status HTTP apropriados

---

## ⚙️ Tecnologias Utilizadas

- Python  
- Flask  
- REST API  
- SQL (banco de dados relacional)  
- Autenticação com JWT  

---

## 🔐 Autenticação

Algumas rotas exigem autenticação via token:


Authorization: Bearer {token_de_acesso}


O token é obtido através do login.

---

## 🔎 Visão Geral dos Endpoints

### 🏨 Hotéis

#### Listar hotéis (com filtros)

GET /hoteis?cidade=&estrelas_min=&estrelas_max=&diaria_min=&diaria_max=&limit=&offset=


#### Buscar hotel por ID

GET /hoteis/{id}


#### Criar hotel (requer autenticação)

POST /hoteis/new


#### Atualizar hotel (requer autenticação)

PUT /hoteis/{id}


#### Deletar hotel (requer autenticação)

DELETE /hoteis/{id}


---

### 👤 Usuários

#### Cadastrar usuário

POST /usuarios/new


#### Login

POST /usuarios/login


#### Logout (requer autenticação)

POST /usuarios/logout


#### Consultar dados do usuário

GET /usuarios/{id}


#### Deletar usuário (requer autenticação)

DELETE /usuarios/{id}


---

### 🌐 Sites

#### Criar site (requer autenticação)

POST /sites/{url}


#### Listar todos os sites

GET /sites


#### Buscar site por URL

GET /sites/{url}


#### Deletar site (requer autenticação)

DELETE /sites/{url}


---

## 🔍 Exemplo de Requisição

### Criar Hotel

```json
POST /hoteis/new
{
  "id": 1,
  "nome": "Inga Hotel",
  "estrelas": 3.5,
  "valor_diaria": 250.9,
  "cidade": "Maringá",
  "site_id": 1
}
📦 Exemplo de Resposta
{
  "id": 1,
  "nome": "Inga Hotel",
  "estrelas": 3.5,
  "valor_diaria": 250.9,
  "cidade": "Maringá",
  "site_id": 1
}
```

## ⚠️ Tratamento de Erros
A API retorna códigos HTTP apropriados:
- 200 OK → Sucesso
- 201 Created → Recurso criado
- 400 Bad Request → Requisição inválida
- 401 Unauthorized → Não autorizado / token inválido
- 404 Not Found → Recurso não encontrado

## 🧠 Conceitos Demonstrados
- Design de APIs RESTful
- Simulação de arquitetura backend
- Autenticação e autorização
- Validação de dados e integridade relacional
- Filtros e paginação de dados
- Tratamento de erros e confiabilidade da API

## 📌 Observações
- Todo hotel deve estar vinculado a um site válido
- Usuários precisam confirmar o e-mail antes de realizar login
- Rotas protegidas exigem token de autenticação

## 💡 Melhorias Futuras
- Documentação com Swagger / OpenAPI
- Containerização com Docker
- Deploy com CI/CD
- Implementação de logs e rate limiting

## 📎 Autor
Projeto desenvolvido com foco em simular um backend real para manipulação e processamento de dados.
