import random as r
import turtle as t
import time as ti

class href():
    def __init__(self):
        
        #initialise screen
        t.setup(900, 900)
        t.color("green")
        snakeheadpos = t.position()
        t.speed(0)


        #movement
        def forward():
            t.pendown()
            t.forward(50)
            t.penup()
        def left():
            t.left(90)
        def right():
            t.right(90)  # Fixed: changed forward(90) to right(90)
        def backward():
            t.backward(50)  # Fixed: changed forward(50) to backward(50)
        def close():
            t.bye()


        #controls

        
        t.onkey(forward, "w")
        t.onkey(left, "a")
        t.onkey(right, "d")
        t.onkey(backward, "s")
        t.onkey(close, "Escape")
        t.listen()

        #spawn positions for cherry
        def cherryinit():
            global currentcherryposx, currentcherryposy
            cherryspawnposx = [0, 50, 100, 150, 200, 250, 300]
            cherryspawnposy = [0, 50, 100, 150, 200, 250, 300]
            t.penup()
            currentcherryposx = r.choice(cherryspawnposx)
            currentcherryposx = float(currentcherryposx)
            print(currentcherryposx)
            currentcherryposy = r.choice(cherryspawnposy)
            currentcherryposy = float(currentcherryposy)
            print(currentcherryposy)

        def rendercherry():
            global snakeheadpos
            t.goto(currentcherryposx, currentcherryposy)
            t.pendown()
            t.fillcolor("red")
            t.begin_fill()
            for x in range(4):
                t.forward(5)
                t.right(90)
            t.end_fill()
            t.penup()

        cherryinit()
        rendercherry()
        #gameloop
        t.goto(0, 0)
        cherryseaten = 0
        while True:
            prevsnakeheadpos = snakeheadpos
            ti.sleep(1)
            t.clear()
            snakeheadpos = t.position()
            rendercherry()
            if cherryseaten == 1:
                snakebody2pos = prevsnakeheadpos
                t.goto(snakebody2pos)
                backward()
                forward()
                t.goto(snakeheadpos)
            if cherryseaten >= 2:
                snakebody2pos = prevsnakeheadpos
                t.goto(snakebody2pos)
                for cherryseaten in range(10):
                
                    backward()
                for cherryseaten in range(10):
                
                    forward()
                t.goto(snakeheadpos)

            elif cherryseaten == 0:
                t.goto(snakeheadpos)
            else:
                t.goto(snakeheadpos)
            forward()
            snakeheadpos = t.position()
            print(snakeheadpos)
            print((currentcherryposx, currentcherryposy))
            t.pencolor("green")
            
            # Fixed collision detection - compare coordinates directly
            if abs(snakeheadpos[0] - currentcherryposx) < 10 and abs(snakeheadpos[1] - currentcherryposy) < 10:
                print("colision detected")
                cherryseaten = cherryseaten + 1
                t.clear()
                cherryinit()
            
href()