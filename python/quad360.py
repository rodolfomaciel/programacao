#! /usr/bin/python
# encoding: utf-8

import turtle

def des_all():
    window = turtle.Screen()
    window.bgcolor('navy')
    des_quad()

    window.exitonclick()

def des_quad():
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('square')
    brad.speed(6)

    for i in range (1,36):
        n=1
        while n <= 4:
            brad.forward(100)
            brad.right(90)
            n += 1
        brad.right(10)

des_all()

    
