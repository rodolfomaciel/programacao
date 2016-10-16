#! /usr/bin/python
# encoding: utf-8
import urllib

def readtext():
    q = open("D:\mac\Github\programacao\python\movie_quotes.txt")
    c = q.read()
    q.close()
    check(c)

def check(c):
    con = urllib.urlopen("http://www.wdylike.appspot.com/?q="+c)
    saida = con.read()
    print(saida)
    con.close()
    if "true" in saida:
        print("Alerta! Alerta! Indecencia encontrada!")
    elif "false" in saida:
        print("Esse documento esta livre de palavras indecentes")
    else:
        print("Nao foi possivel escanear o documento")

readtext()
    
    
