select ordernames.name, count(*) as num
  from animals, taxonomy, ordernames
  where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc
------------------------------------------------------
select ordernames.name, count(*) as num
  from (animals join taxonomy 
                on animals.species = taxonomy.name)
                as ani_tax
        join ordernames
             on ani_tax.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc
------------------------------------------------------
select food, count(animals.name) as num
       from diet join animals 
       on diet.species = animals.species
       group by food
       having num = 1
------------------------------------------------------   
 select food, count(animals.name) as num
       from diet, animals 
       where diet.species = animals.species
       group by food
       having num = 1
------------------------------------------------------          
insert into table ( column1, column2, ... ) values ( val1, val2, ... );
insert into table values ( val1, val2, ... );

------------------------------------------------------   
------------------------------------------------------   
------------------------------------------------------   
------------------------------------------------------   
------------------------------------------------------   
------------------------------------------------------   
