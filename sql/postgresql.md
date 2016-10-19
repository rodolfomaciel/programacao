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

##Conceitos Básicos
- Organização dos arquivos de dados
 - Grupos de bancos (Cluster)
  - Banco de dados (Database)
   - Tabelas (Table)
    - Rows (Linhas)
     - Columns (Colunas)
     
     
##Tabelas
- Criar tabelas.
    CREATE TABLE weather (
        city            varchar(80),
        temp_lo         int,           -- low temperature
        temp_hi         int,           -- high temperature
        prcp            real,          -- precipitation
        date            date
    );

- Deletar tabela:
DROP TABLE tablename;
    
- Inserindo dados:
INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');

- Inserir dados a partir de um arquivo:
COPY weather FROM '/home/user/weather.txt';

    
