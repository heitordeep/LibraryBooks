# LibraryBooks
## CRUD de Sistema de Biblioteca. Utilizado: Python 3.7.3, Django 2.2.6 e SQLite 3


Para iniciar o projeto você precisa ter instalado na sua maquina o pyenv e utilizar a versão 3.7 do Python.

## Inicialização:


1° Após clonar o projeto basta digitar.
 ```shell
 $ source venv/bin/activate
 ```
Não se preocupe, no diretório possui a pasta da virtualização venv.


2° Você precisa iniciar o servidor.
  ```shell
  $ python manage.py runserver
  ```
  
## Acessando o APP:

Após digitar os comandos a cima, basta acessar a URL: http://127.0.0.1:8000/books/login

    Login: visitante
    Senha: 123@2019

## Funcionalidades:

Após logado, você será redirecionado para a página home do site, onde você terá a visão de todos os estudantes que alugaram os livros da biblioteca.
Na tela administrativa do sistema você possui telas de: editar, deletar, atualizar e visualizar com mais detalhes os dados dos estudantes.

- O sistema de CRUD foi desenvolvimento por classes genéricas do Django

- Este projeto foi desenvolvido para fins de estudos.
