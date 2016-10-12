##Como usar select

select ordernames.name, count(*) as num
  from animals, taxonomy, ordernames
  where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc


select ordernames.name, count(*) as num
  from (animals join taxonomy 
                on animals.species = taxonomy.name)
                as ani_tax
        join ordernames
             on ani_tax.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc



       
SELECT colunas, count(asterisco), min(), max()
FROM tabelas
WHERE condições, AND, OR, NOT
GROUP BY agrupar
ORDER BY ordenar, DESC decrescente
LIMIT limitar
OFFSET a partir de

##Como usar insert into
insert into table ( column1, column2, ... ) values ( val1, val2, ... );
insert into table values ( val1, val2, ... );


##Como criar tabelas
create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);
       
create table tablename (column1 type [constraints], column1 type [constraints], ..., columnN type [constraints]);

###Relacionamentos
create table sales(id text references products(id), sales_date date, count integer);
       
       
##Como usar join

select food, count(animals.name) as num
       from diet join animals 
       on diet.species = animals.species
       group by food
       having num = 1


 select food, count(animals.name) as num
       from diet, animals 
       where diet.species = animals.species
       group by food
       having num = 1
