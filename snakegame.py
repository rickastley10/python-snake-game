import random as r
import turtle as t
import time as ti

class href():
    def __init__(self):
        # Initialize screen
        t.setup(900, 900)
        t.color("green")
        t.speed(0)
        t.penup()
        
        # Snake properties
        self.snake_segments = [t.Turtle() for _ in range(3)]  # Initial snake with 3 segments
        for i, segment in enumerate(self.snake_segments):
            segment.shape("square")
            segment.color("green")
            segment.penup()
            segment.goto(0, -i * 20)  # Position segments vertically
        
        self.head = self.snake_segments[0]
        self.direction = "up"
        self.cherryseaten = 0
        
        # Cherry initialization
        self.cherry = t.Turtle()
        self.cherry.shape("square")
        self.cherry.color("red")
        self.cherry.penup()
        self.cherry_init()
        
        # Controls
        t.onkey(lambda: self.set_direction("up"), "w")
        t.onkey(lambda: self.set_direction("left"), "a")
        t.onkey(lambda: self.set_direction("right"), "d")
        t.onkey(lambda: self.set_direction("down"), "s")
        t.onkey(t.bye, "Escape")
        t.listen()
        
        # Game loop
        self.game_loop()
    
    def set_direction(self, new_direction):
        # Prevent 180-degree turns
        if (new_direction == "up" and self.direction != "down") or \
           (new_direction == "down" and self.direction != "up") or \
           (new_direction == "left" and self.direction != "right") or \
           (new_direction == "right" and self.direction != "left"):
            self.direction = new_direction
    
    def move_snake(self):
        # Move the body segments (from tail to head)
        for i in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[i-1].xcor()
            y = self.snake_segments[i-1].ycor()
            self.snake_segments[i].goto(x, y)
        
        # Move the head based on direction
        if self.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.direction == "right":
            self.head.setx(self.head.xcor() + 20)
    
    def cherry_init(self):
        cherryspawnposx = list(range(-400, 401, 20))
        cherryspawnposy = list(range(-400, 401, 20))
        x = r.choice(cherryspawnposx)
        y = r.choice(cherryspawnposy)
        self.cherry.goto(x, y)
    
    def check_collision(self):
        # Check collision with cherry
        if self.head.distance(self.cherry) < 20:
            self.cherryseaten += 1
            self.cherry_init()
            
            # Add new segment to snake
            new_segment = t.Turtle()
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(self.snake_segments[-1].position())
            self.snake_segments.append(new_segment)
        
        # Check collision with walls
        if (self.head.xcor() > 440 or self.head.xcor() < -440 or 
            self.head.ycor() > 440 or self.head.ycor() < -440):
            self.game_over()
        
        # Check collision with self
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                self.game_over()
    
    def game_over(self):
        t.clearscreen()
        t.penup()
        t.goto(0, 0)
        t.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        t.goto(0, -50)
        t.write(f"Score: {self.cherryseaten}", align="center", font=("Arial", 18, "normal"))
        ti.sleep(3)
        t.bye()
    
    def game_loop(self):
        while True:
            self.move_snake()
            self.check_collision()
            ti.sleep(0.2)

# Start the game
href()
