#! /usr/bin/python
# encoding: utf-8

class Clientes(object):
	def __init__(self, email, cel):
		self.email = email
		self.cel = cel

	def __repr__(self):
		print("Minha classe cliente")