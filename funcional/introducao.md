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

    function grandParent(g1, g2) {
        var g3 = 3;
        return function parent(p1, p2) {
            var p3 = 33;
            return function child(c1, c2) {
                var c3 = 333;
                return g1 + g2 + g3 + p1 + p2 + p3 + c1 + c2 + c3;
            };
        };
    }
    
    
###Composição

Usar várias funções para realizar uma tarefa.

    var add10 = value => value + 10;
    var mult5 = value => value * 5;
    var mult5AfterAdd10 = value => 5 * (value + 10)
    
###Currying

Funções encadeadas que recebem apenas um parâmetro

    var compose = (f, g) => x => f(g(x));
    var mult5AfterAdd10 = compose(mult5, add(10));
    
###Funções padrões

Map, filter, reduce.

###Transparencia referencial

Trocar a função pelo código bruto.

###Ordem de execução

Execução única, execução paralela.

###Notação de tipos de dados

    add : Int -> Int -> Int
    add x y =
         x + y


    
