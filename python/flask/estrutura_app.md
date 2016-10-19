Estrutura básica de aplicacação flask

    /application
        -run.py
            # from yourapplication import app
            # app.run(debug=True)    
        /application
            -__init__.py - o arquivo de inicialização da applicacao
                # from flask import Flask
                # app = Flask(__name__)
                # import application.views
                #applicaction.py - aqui vao os controladores da app
            -views.py - aqui vao as funcoes de visualização
                # from application import app
                # @app.route('/')
                # def index():
                #    return 'Hello World!'
            -schema.sql - aqui voce coloca o design do banco de dados
            /static
                -style.css
            /templates
                -layout.html
                -index.html
                -login.html
