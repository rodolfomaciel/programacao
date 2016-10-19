#Resumo Doc Postgre

##Operações Básicas
- Instalação - $ apt-get install postgresql-9.6 - ou então:
 - ./configure
 - make
 - su
 - make install
 - adduser postgres
 - mkdir /usr/local/pgsql/data
 - chown postgres /usr/local/pgsql/data
 - su - postgres
 - /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
 - /usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data >logfile 2>&1 &
 - /usr/local/pgsql/bin/createdb test
 - /usr/local/pgsql/bin/psql test
- **Criar** banco de dados - $ createdb mydb
- Criar banco de dados com o mesmo nome do usuário - $ createdb
- **Deletar** banco de dados - $ dropdb mydb
- **Acessando** o banco de dados - $ psql mydb
- Pedindo ajuda sobre um comando - $ mydb=> \h
- Para **sair** o banco de dados - $ mydb=> \q

