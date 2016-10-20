Estrutura básica de aplicacação flask

    /Larger_App
        |--setup.cfg
            
        |--setup.py
                from setuptools import setup

                setup(
                    name='flaskr',
                    packages=['flaskr'],
                    include_package_data=True,
                    install_requires=[
                        'flask',
                    ],
                    setup_requires=[
                        'pytest-runner',
                    ],
                    tests_require=[
                        'pytest',
                    ],
                )
        |--config.py
                # Statement for enabling the development environment
                DEBUG = True

                # Define the application directory
                import os
                BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

                # Define the database - we are working with
                # SQLite for this example
                SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
                DATABASE_CONNECT_OPTIONS = {}

                # Application threads. A common general assumption is
                # using 2 per available processor cores - to handle
                # incoming requests using one and performing background
                # operations using the other.
                THREADS_PER_PAGE = 2

                # Enable protection agains *Cross-site Request Forgery (CSRF)*
                CSRF_ENABLED     = True

                # Use a secure, unique and absolutely secret key for
                # signing the data. 
                CSRF_SESSION_KEY = "secret"

                # Secret key for signing cookies
                SECRET_KEY = "secret"
        |--run.py
                # from application import app
                # app.run(host='0.0.0.0', port=8080, debug=True)
        |__env/
        |__/application
            |--__init__.py - o arquivo de inicialização da applicacao
                    # from flask import Flask
                    # app = Flask(__name__)
                    # import application.views
                    #applicaction.py - aqui vao os controladores da app
            |__/mod_auth
                |-- __init__.py
                |-- controllers.py
                |-- models.py
                |-- forms.py
            |__/templates
                |__/mod_auth
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

