###Funcoes puras

Funcoes que retornam um valor puro. Exemplo em js:

    function add(x,y){return x + y;} //retorna a soma de x e y
    
    function justTen() {return 10;} //10
    
As funcoes puras devem receber pelo menos um parametro e retornar um valor
Para valores de parametros iguais a funcao pura sempre retorna o mesmo resultado
Elas não tem nenhum efeito colateral

###Funcoes impuras

São as que lidam com variaveis externas e modificam valores, como por exemplo,
alterar um arquivo, atualizar um banco de dados, enviar dados a um servidor e etc.

Linguagens funcionais não conseguem eliminar efeitos colaterais
elas so conseguem confina-las.

###Imutabilidade

Não existem variaveis na programação funcional, apenas constantes.

A recursao substitui o looping na programação funcional. Exemplo em elm:

    sumRange start end acc =
    if start > end then
        acc
    else
        sumRange (start + 1) end (acc + start) 

Se um pedaço do programa quiser mudar um valor ele terá de
criar outro valor modificando o antigo.

    a = 1
    b = a + 1 //2




