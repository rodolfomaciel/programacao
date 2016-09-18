#! /usr/bin/python
# encoding: utf-8
import os


def renomear_arquivos():
	fl = os.listdir("/home/rodolfo/codings/programacao/python/prank")
	sp = os.getcwd()
	os.chdir("/home/rodolfo/codings/programacao/python/prank")
	for i in fl:
		print("Nome anterior"+ i)
		print("Novo nome"+ i.translate(None, "0123456789"))
		os.rename(i, i.translate(None, "0123456789"))
	os.chdir(sp)

renomear_arquivos()