#! /usr/bin/python
# codings: utf-8
"""
Usando o modulo random
"""

from random import *

print("Escolhendo um numero inteiro de 0 a 100: ", randint(0,100))
print("Escolhendo um numero real de 0 a 100: ", uniform(0,100))
p = ['anderson', 'eric', 'diego', 'felipe', 'yuri', 'delio', 'rodolfo', 'rayssa', 'andre', 'jessica', 'ronne', 'italo', 'luan', 'perboyre']
print("Essa é a lista inicial: \n ", p)
n = randint(1,14)
print("O numero escolhido foi: \n ", n)
shuffle(p)
print("Misturando a lista a primeira vez: \n ", p)
print("Escolhendo os %i items da lista: \n" %n, sample(p,n))
shuffle(p)
print("Embaralhando a lista novamente: \n ", p)
print("Escolhendo o item vencedor:", sample(p, 1))
