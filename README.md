## Python FastAPI REST

```
Python
python: 3.9.2
pip: 20.3.1
```
1. [Instalação](#installation)
2. [Inicializando a aplicação](#run-app)
    1. [Local](#run-app-local)
    2. [Docker](#run-app-docker)
3. [Testes](#run-tests)
    1. [Local](#run-tests-local)
    2. [Docker](#run-tests-docker)
4. [Estrutura do Projeto](#concept-of-structure)
    1. [Sobre src/controllers](#controllers-folder)
    2. [Sobre src/services](#services-folder)
    3. [Sobre src/tests](#tests-folder)
5. [Swagger](#swagger)
6. [Dependências do Projeto](#project-dependencies)


## Instalação

Para instalar as dependências do projeto utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  pip install -r requirements.txt
```


## Inicializando a aplicação

### Local

Para inicializar a aplicação localmente utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  uvicorn src.main:app --reload --port 8080
```

### Docker
Para inicializar a aplicação através do [Docker](https://docs.docker.com/) utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  sudo docker-compose up -d --build
```

Caso o container não inicialize, utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  sudo docker-compose up -d
```

## Testes

### Local

Para inicializar os testes localmente utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  pytest src/tests/test.py
```

### Docker
Para inicializar os testes através do [Docker](https://docs.docker.com/) utilize o comando demonstrado a seguir na raiz do diretório:

```sh
  sudo docker-compose exec app pytest src/tests/test.py
```

## Estrutura do projeto

```
└── src
    ├── controllers
    │   ├── healthcheck.py
    │   ├── home.py
    ├── services
    │   ├── healthcheck.py
    │   ├── home.py
    └── tests
    |    └── test.py
    ├── main.py
```

### Diretório **src/controllers**

O diretório de `src/controllers` é responsável por controlar a comunicação entre as requisições feitas do cliente para com a aplicação.


### Diretório **src/services**

O diretório `src/services` é responsável pela manipulação dos dados que serão recebidos e enviados pelos `controllers`.

### Diretório **src/tests**

O diretório `src/tests` contém os testes das entradas e saídas dos `controllers`.

## Swagger
O FastAPI já vêm com o Swagger embutido, sendo `/docs` uma versão mais simplificada e `/redoc` uma versão mais completa. Para adicionar as informações basta apenas a criação dos `endpoints` e então é possível visualizá-los através dos endereços demonstrados a seguir:

- Swagger Local [/redoc](http://127.0.0.1:8080/redoc)
- Swagger Local [/docs](http://127.0.0.1:8080/docs)

- Swagger Docker [/redoc](http://0.0.0.0:8080/redoc)
- Swagger Docker [/docs](http://0.0.0.0:8080/docs)

## Dependências do Projeto

- [fastapi](https://fastapi.tiangolo.com/): Framework para criação das APIs REST.
- [fastapi-health](https://pypi.org/project/fastapi-health/): Biblioteca para realizar healthcheck das rotas.
- [uvicorn](https://www.uvicorn.org/): Servidor ASGI.
- [pytest](https://docs.pytest.org/en/6.2.x/): Framework responsável por automatizar testes.
- [requests](https://pypi.org/project/requests/): Biblioteca para realizar requisições HTTP/HTTPS.
