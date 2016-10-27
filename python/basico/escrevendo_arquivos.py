#! /usr/bin/python
# codings: utf-8

import os
import os.path

#Criando arquivo
fn = 'teste.py'
mf = open(fn, 'w')
mf.write('Escrevendo minha primeira linha com Python\n')
mf.close()
mf = open(fn,'r')
mf.readlines()
mf.close()

#Adicionando mais uma linha
mf = open(fn, 'a')
mf.write('Adicionando outra linha ao meu arquivo\n')
mf.close()
mf = open(fn,'r')
mf.readlines()
mf.close()

"""
r 	leitura
w 	leitura e escrita
b 	modo binario
r+ 	leitura e escrita
a+ 	adiciona ao final
w+ 	leitura e escrita 
"""
