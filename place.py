import game

game.placelock=0

def checkplace(x,y):
    if x == 0 and y == 0:
        if game.f00 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 0 and y == 1:
        if game.f01 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 0 and y == 2:
        if game.f02 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 1 and y == 0:
        if game.f10 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 1 and y == 1:
        if game.f11 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 1 and y == 2:
        if game.f12 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 2 and y == 0:
        if game.f20 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 2 and y == 1:
        if game.f21 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
    if x == 2 and y == 2:
        if game.f22 != "dummy":
            game.placelock=1
        else:
            game.placelock=0
