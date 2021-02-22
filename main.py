import game
import win
import place
import setup

game.setuplock=0
setup.setup()

def changepos(d):
    if game.movelock==0:
        game.movelock=1
        game.placelock=1
        if d==1:
            if game.y < 2:
                print("up")
                game.y=game.y+1
                game.sety((game.y*game.edge+game.edge/2)-1.5*game.edge)
        if d==2:
            if game.y > 0:
                print("down")
                game.y=game.y-1
                game.sety((game.y*game.edge+game.edge/2)-1.5*game.edge)
        if d==3:
            if game.x > 0:
                print("left")
                game.x=game.x-1
                game.setx((game.x*game.edge+game.edge/2)-1.5*game.edge)
        if d==4:
            if game.x < 2:
                print("right")
                game.x=game.x+1
                game.setx((game.x*game.edge+game.edge/2)-1.5*game.edge)
        game.movelock=0
        checkpos()

def checkpos():
    if game.y<0:
        changepos(1)
    if game.y>2:
        changepos(2)
    if game.x>2:
        changepos(3)
    if game.x<0:
        changepos(4)
    place.checkplace(game.x, game.y)

def draw():
    if game.placelock==0:
        game.setuplock=1
        game.placelock=1
        game.movelock=1
        if game.last==2:
            game.drawX(game.x,game.y)
            game.last=1
        elif game.last==1:
            game.drawO(game.x,game.y)
            game.last=2
        assign(game.x,game.y,game.last)
        game.movelock=0
        game.setuplock=0

def assign(x,y,p):
    if x==0 and y==0:
        game.f00=p
    if x==0 and y==1:
        game.f01=p
    if x==0 and y==2:
        game.f02=p
    if x==1 and y==0:
        game.f10=p
    if x==1 and y==1:
        game.f11=p
    if x==1 and y==2:
        game.f12=p
    if x==2 and y==0:
        game.f20=p
    if x==2 and y==1:
        game.f21=p
    if x==2 and y==2:
        game.f22=p
    win.checkwin(p)

game.listen()
game.onkey(lambda:changepos(1),'Up')
game.onkey(lambda:changepos(2),'Down')
game.onkey(lambda:changepos(3),'Left')
game.onkey(lambda:changepos(4),'Right')
game.onkey(lambda:draw(),'Return')
game.onkey(lambda:setup.setup(),'s')
game.mainloop()
