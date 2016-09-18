#! /usr/bin/python

import time
import webbrowser

x=0
while x <  3:
	time.sleep(60)
	webbrowser.open("https://www.youtube.com/watch?v=_WcWHZc8s2I&list=PL6CB08BA1FA4C3E44")
	x += 1
	print("Vezes executada: ", x)