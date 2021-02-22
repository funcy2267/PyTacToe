from turtle import *

setup(width=500,height=500)

def kwadrat():
    pencolor("black")
    pd()
    for i in range(4):
        fd(edge)
        left(90)
    pu()

def plansza():
    pu()
    bk(1.5*edge)
    right(90)
    fd(1.5*edge)
    left(90)
    pd()
    for i in range(3):
        for j in range(3):
            pd()
            kwadrat()
            pu()
            fd(edge)
        bk(3*edge)
        left(90)
        fd(edge)
        right(90)
    pu()

def drawX(a,b):
    print("x")
    pencolor("blue")
    pu()
    setx((a*edge+edge/2)-1.5*edge)
    sety((b*edge+edge/2)-1.5*edge)
    pd()
    left(45)
    for i in range (4):
        fd(edge/4)
        bk(edge/4)
        left(90)
    right(45)
    pu()

def drawO(a,b):
    print("o")
    pencolor("red")
    pu()
    setx((a*edge+edge/2)-1.5*edge)
    sety((b*edge+edge/2-edge/4)-1.5*edge)
    pd()
    circle(edge/4)
    pu()
    sety((b*edge+edge/2)-1.5*edge)
