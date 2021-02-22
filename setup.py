import game

def setup():
    if game.setuplock == 0:
        game.setuplock=1
        game.movelock=1
        game.placelock=1
        game.reset()
        game.pu()
        game.clear()
        game.pensize(5)
        game.edge=80
        game.sety(0)
        game.setx(0)
        game.title("PyTacToe")
        game.speed(0)
        game.plansza()
        game.speed(2)
        game.sety(0)
        game.setx(0)
        game.x=1
        game.y=1
        game.last=2
        print("x - 1")
        print("o - 2")
        game.f00=game.f01=game.f02=game.f10=game.f11=game.f12=game.f20=game.f21=game.f22="dummy"
        game.setuplock=0
        game.movelock=0
        game.placelock=0
