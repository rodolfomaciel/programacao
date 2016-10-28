#! /usr/bin/pyhton
# codings: utf-8

"""
Nesta funcao sum voce pode passar diversos numero
"""
def sum(*arg): 
    r=0
    for i in arg:
        r+=i
    return r
