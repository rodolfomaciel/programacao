/application
    -run.py
    #from yourapplication import app
    #app.run(debug=True)    
    /application
        -__init__.py
        #from flask import Flask
        #app = Flask(__name__)
        #import application.views
        -views.py
        #from application import app
        #@app.route('/')
        #def index():
        #    return 'Hello World!'
        /static
            -style.css
        /templates
            -layout.html
            -index.html
            -login.html
