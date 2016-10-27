#! /usr/bin/python
# codings: utf-8

a = 10  # variavel global
print(a)

def local():
	global c # variavel local configurada como global
	a = 8 # variavel local
	print(a)
	c = 5
	
	
local()

c -= 1
a += 1
print(a, c)
