#! /usr/bin/python
# codings: utf-8

"""
Encapsulation - esconder informações
"""

class Escondido(object):
	def __init__(self):
		self.__criar()
		
	def __criar(self):
		print("Usando Encapsulation")

	
r = Escondido()
r.__criar() #Vai dar erro nessa linha pois o metodo __criar() não pode ser acessado
