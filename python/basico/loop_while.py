#!/usr/bin/python
# codings: utf-8

l = []
ad = 's'

while ad == 's':
	l.append(input("Digite item: "))
	ad = input(str("Deseja continuar? s ou n?"))

print("A lista digitada é ", l)
