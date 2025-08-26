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
        movementlist = []
        snake_segments = []  # Store positions of snake segments

        #movement
        def forward():
            t.pendown()
            t.forward(50)
            t.penup()
            # Add current position to segments
            snake_segments.append(t.position())
            # Keep only the last few segments based on cherries eaten
            if len(snake_segments) > cherryseaten + 1:
                snake_segments.pop(0)
            
        def left():
            movementlist.append("left")
            t.left(90)
        def right():
            movementlist.append("right")
            t.right(90)
        def backward():
            t.backward(50)
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
            # Save current position first
            current_pos = t.position()
            t.penup()
            t.goto(currentcherryposx, currentcherryposy)
            t.pendown()
            t.fillcolor("red")
            t.begin_fill()
            for x in range(4):
                t.forward(5)
                t.right(90)
            t.end_fill()
            t.penup()
            # Return to original position
            t.goto(current_pos)

        def draw_snake_body():
            # Draw all snake body segments
            current_pos = t.position()
            for segment_pos in snake_segments[:-1]:  # Skip the head
                t.penup()
                t.goto(segment_pos)
                t.pendown()
                t.fillcolor("green")
                t.begin_fill()
                for x in range(4):
                    t.forward(5)
                    t.right(90)
                t.end_fill()
                t.penup()
            t.goto(current_pos)

        cherryinit()
        rendercherry()
        #gameloop
        t.goto(0, 0)
        cherryseaten = 0
        while True:
            print("Movement list:", movementlist)
            print("Snake segments:", len(snake_segments))
            prev_pos = t.position()
            ti.sleep(1)
            t.clear()
            rendercherry()
            
            # Draw snake body
            draw_snake_body()
            
            # Move forward
            forward()
            current_pos = t.position()
            
            print("Head position:", current_pos)
            print("Cherry position:", (currentcherryposx, currentcherryposy))
            t.pencolor("green")
            
            # Fixed collision detection - compare coordinates directly
            if abs(current_pos[0] - currentcherryposx) < 10 and abs(current_pos[1] - currentcherryposy) < 10:
                print("collision detected")
                cherryseaten = cherryseaten + 1
                # Add more segments when cherry is eaten
                for i in range(3):  # Add 3 segments per cherry
                    snake_segments.append(current_pos)
                t.clear()
                cherryinit()
            
href()
