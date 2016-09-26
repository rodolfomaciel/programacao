#! /usr/bin/python
# encoding: utf-8

import turtle

def des_all():
    window = turtle.Screen()
    window.bgcolor('navy')
    des_quad()
    des_circ()
    des_tri()

    window.exitonclick()


def des_quad():
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed(3)

    n=1
    while n <= 4:
        brad.forward(100)
        brad.right(90)
        n += 1

def des_circ():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("white")
    angie.circle(100)

def des_tri():    
    fido = turtle.Turtle()
    fido.shape("circle")
    fido.color("red")
    fido.speed(2)
    n=1
    while n <=3:
        fido.forward(120)
        fido.left(120)
        n += 1

des_all()
