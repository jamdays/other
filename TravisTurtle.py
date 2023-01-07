from turtle import *


def drawSquare (t,side):
    t.fd(side)
    t.rt(90)
    t.fd(side)
    t.rt(90)
    t.fd(side)
    t.rt(90)
    t.fd(side)
    t.rt(90)

def main():
    t = Turtle()
    drawSquare(t,200)
    t.color('yellow')
    drawSquare(t,100)
    t.color('blue')
    drawSquare(t,400)
    
