#! /usr/bin/python
# codings: utf-8

"""
Encapsulation - esconder informações
"""

class Escondido(object):
	__acao=""
	
	def __init__(self):
		self.__acao="Nao quero aparecer"
		self.__criar()
	
	def set_acao(self, acao):
		self.__acao = acao
		
	def __criar(self):
		print("Usando Encapsulation")
	
r = Escondido()
r.__criar() #Vai dar erro nessa linha pois o metodo __criar() não pode ser acessado
