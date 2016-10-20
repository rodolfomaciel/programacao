Estrutura básica de aplicacação flask

    /Larger_App
        |--config
        |--run.py
            # from yourapplication import app
            # app.run(debug=True)
        |__env/
        |__/application
            |--__init__.py - o arquivo de inicialização da applicacao
                    # from flask import Flask
                    # app = Flask(__name__)
                    # import application.views
                    #applicaction.py - aqui vao os controladores da app
            |__/module_one
                |-- __init__.py
                |-- controllers.py
                |-- models.py
            |__/templates
                |__/module_one
                    |-- hello.html
                    |--layout.html
                    |--index.html
                    |--login.html
            |__/static
                |--style.css
            
            
            
            |--views.py - aqui vao as funcoes de visualização
                # from application import app
                # @app.route('/')
                # def index():
                #    return 'Hello World!'
            |--schema.sql - aqui voce coloca o design do banco de dados

