Instalacao Apache2
- $ sudo apt-get install apache2
- $ sudo apt-get install python-setuptools libapache2-mod-wsgi
- $ sudo service apache2 restart
- $ sudo vi /etc/apache2/apache2.conf
- Adicione ServerName localhost


Instalacao Postgre
- $ sudo apt-get install postgresql postgresql-contrib
- $ sudo adduser (nome do usuario)
- $ psql
- # CREATE USER catalog WITH PASSWORD 'PW-FOR-DB';
- # ALTER USER catalog CREATEDB;
- # CREATE DATABASE catalog WITH OWNER catalog;
- # \c catalog
- # REVOKE ALL ON SCHEMA public FROM public;
- # GRANT ALL ON SCHEMA public TO catalog;
- # \q e $ exit

Instalacao Git
- $ sudo apt-get install git
- $ git config --global user.name "YOUR NAME"
- $ git config --global user.email "YOUR EMAIL ADDRESS"

Instalacao Flask
- $ sudo apt-get install libapache2-mod-wsgi python-dev
- $ sudo a2enmod wsgi
- Crie a estrutura do aplicativo
- $ sudo apt-get install python-pip
- $ sudo pip install virtualenv
- $ sudo virtualenv venv
- $ sudo chmod -R 777 venv
- $ source venv/bin/activate
- $ pip install Flask
- $ deactivate

Crie um virtual host
- $ sudo nano /etc/apache2/sites-available/catalog.conf

    <VirtualHost *:80>
      ServerName PUBLIC-IP-ADDRESS 
      ServerAdmin admin@PUBLIC-IP-ADDRESS 
      WSGIScriptAlias / /var/www/catalog/catalog.wsgi 

      <Directory /var/www/catalog/catalog/>
        Order allow,deny     
        Allow from all 
      </Directory> 

      Alias /static /var/www/catalog/catalog/static 

      <Directory /var/www/catalog/catalog/static/>     
        Order allow,deny
        Allow from all 
      </Directory>

      ErrorLog ${APACHE_LOG_DIR}/error.log 
      LogLevel warn 
      CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>

Ative o virtual host
- $ sudo a2ensite catalog

CRie o arquivo wsgi
- $ cd /var/www/catalog
- $ sudo vim catalog.wsgi

    #!/usr/bin/python
    import sys
    import logging

    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/catalog/catalog/venv")

    from catalog import app as application

Reinicie o apache
$ sudo service apache2 restart




