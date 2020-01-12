# LibraryBooks
## CRUD de Sistema de Biblioteca. Utilizado: Python 3.7.3, Django 2.2.6 e SQLite 3


Para iniciar o projeto você precisa ter instalado na sua maquina o virtualenv e utilizar a versão 3.7 do Python.

## Inicialização:

1° Instalação.
```shell
 $ pip install -r requirements.txt
```

2° Inicialização do CRUD.

 ```shell
 $ source venv/bin/activate
 ```

3° Iniciar o servidor.
  
  ```shell
  $ python manage.py runserver
  ```
  
## Acessando o APP:

Após digitar os comandos a cima, basta acessar a URL: http://127.0.0.1:8000/books/login

    Login: visitante 
    Senha: admin@123

Ou você pode fazer um teste online neste link: https://library-study.herokuapp.com/login/

    Login: visitante
    Senha: admin@123

Ou você pode fazer um teste online neste link: https://library-study.herokuapp.com/login/

    Login: visitante
    Senha: admin@123

## Funcionalidades:

Após logado, você será redirecionado para a página home do site, onde você terá a visão de todos os estudantes que alugaram os livros da biblioteca.
Na tela administrativa do sistema você possui telas de: editar, deletar, atualizar e visualizar com mais detalhes os dados dos estudantes.

- O sistema de CRUD foi desenvolvimento por classes genéricas do Django

- Este projeto foi desenvolvido para fins de estudos.
