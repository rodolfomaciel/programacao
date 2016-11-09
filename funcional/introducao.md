###Funções puras

Funcoes que retornam um valor puro. Exemplo em js:

    function add(x,y){return x + y;} //retorna a soma de x e y
    
    function justTen() {return 10;} //10
    
As funcoes puras devem receber pelo menos um parametro e retornar um valor
Para valores de parametros iguais a funcao pura sempre retorna o mesmo resultado
Elas não tem nenhum efeito colateral

###Funções impuras

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

###Refatorar

As duas funções a seguir podem ser refatoradas e simplificadas:

    function validateSsn(ssn) {
    if (/^\d{3}-\d{2}-\d{4}$/.exec(ssn))
        console.log('Valid SSN');
    else
        console.log('Invalid SSN');
    }

    function validatePhone(phone) {
        if (/^\(\d{3}\)\d{3}-\d{4}$/.exec(phone))
            console.log('Valid Phone Number');
        else
            console.log('Invalid Phone Number');
    }
    
Elas poderiam ser 'unificadas' na seguinte função:

    function validateValue(value, regex, type) {
    if (regex.exec(value))
        console.log('Invalid ' + type);
    else
        console.log('Valid ' + type);
    }

###Função de ordem superior

É aquela que recebe uma função como argumento e/ou retorna uma função como resultado.

    function makeRegexParser(regex) {
        return regex.exec;
    }

###Closure

São funções aninhadas ou aprisionadas dentro de outras funções.


    
