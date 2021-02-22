import game
import setup
import time

def afterwin():
    game.pu()
    time.sleep(1.5)
    game.setuplock=0
    setup.setup()

def checkwin(last):
    if game.f00 != "dummy" and game.f10 != "dummy" and game.f20 != "dummy":
        if game.f00 == last:
            if game.f10 == last:
                if game.f20 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.ywin=0
                    game.pd()
                    game.sety((game.ywin*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((-1*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((3*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f01 != "dummy" and game.f11 != "dummy" and game.f21 != "dummy":
        if game.f01 == last:
            if game.f11 == last:
                if game.f21 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.ywin=1
                    game.pd()
                    game.sety((game.ywin*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((-1*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((3*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f02 != "dummy" and game.f12 != "dummy" and game.f22 != "dummy":
        if game.f02 == last:
            if game.f12 == last:
                if game.f22 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.ywin=2
                    game.pd()
                    game.sety((game.ywin*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((-1*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((3*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f00 != "dummy" and game.f01 != "dummy" and game.f02 != "dummy":
        if game.f00 == last:
            if game.f01 == last:
                if game.f02 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.xwin=0
                    game.pd()
                    game.sety((3*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((game.xwin*game.edge+game.edge/2)-1.5*game.edge)
                    game.sety((-1*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f10 != "dummy" and game.f11 != "dummy" and game.f12 != "dummy":
        if game.f10 == last:
            if game.f11 == last:
                if game.f12 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.xwin=1
                    game.pd()
                    game.sety((3*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((game.xwin*game.edge+game.edge/2)-1.5*game.edge)
                    game.sety((-1*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f20 != "dummy" and game.f21 != "dummy" and game.f22 != "dummy":
        if game.f20 == last:
            if game.f21 == last:
                if game.f22 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.xwin=2
                    game.pd()
                    game.sety((3*game.edge+game.edge/2)-1.5*game.edge)
                    game.setx((game.xwin*game.edge+game.edge/2)-1.5*game.edge)
                    game.sety((-1*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f00 != "dummy" and game.f11 != "dummy" and game.f22 != "dummy":
        if game.f00 == last:
            if game.f11 == last:
                if game.f22 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.pd()
                    game.setpos((3*game.edge+game.edge/2)-1.5*game.edge, (3*game.edge+game.edge/2)-1.5*game.edge)
                    game.setpos((-1*game.edge+game.edge/2)-1.5*game.edge, (-1*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f02 != "dummy" and game.f11 != "dummy" and game.f20 != "dummy":
        if game.f02 == last:
            if game.f11 == last:
                if game.f20 == last:
                    if last == 1:
                        game.pencolor("blue")
                    if last == 2:
                        game.pencolor("red")
                    game.pd()
                    game.setpos((-1*game.edge+game.edge/2)-1.5*game.edge, (3*game.edge+game.edge/2)-1.5*game.edge)
                    game.setpos((3*game.edge+game.edge/2)-1.5*game.edge, (-1*game.edge+game.edge/2)-1.5*game.edge)
                    afterwin()
    if game.f00 != "dummy" and game.f01 != "dummy" and game.f02 != "dummy" and game.f10 != "dummy" and game.f11 != "dummy" and game.f12 != "dummy" and game.f20 != "dummy" and game.f21 != "dummy" and game.f22 != "dummy":
        afterwin()
