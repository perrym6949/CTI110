# START
import turtle
import random

# WIN WITH BACKGROUND COLOR
win = turtle.Screen()
win.bgcolor("white")
t = turtle.Turtle()
t.speed(20)

# COLOR LIST
sfcolor = ["dark red", "black", "purple", "green", "pink"]

#SIZE FUNCTION
def snowflake(size):   # Size and location of snowflake on page will differ 
    t.penup()
    t.forward(10*size)
    t.left(45)
    t.pendown()
    t.color(random.choice(sfcolor))
    for i in range(8):
        branch(size)
        t.left(45)
        
# BRANCH STRUCTURE
def branch(size):
    for i in range(3):
        for i in range(3):
            t.forward(10.0*size/3)
            t.backward(10.0*size/3)
            t.right(45)
        t.left(90)
        t.backward(10.0*size/3)
        t.left(45)
    t.right(90)
    t.forward(10.0*size)

# DRAW FIVE RANDOM SNOWFLAKES
for i in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    t.penup()
    t.goto(x, y)
    t.pendown()
    snowflake(sf_size)
    
# END COMMANDS
win.mainloop()


# REFERENCE

# THIS PROGRAM WAS INSPIRED BY:

# Geek Gurl Diaries Episode 33: Xmas Special Make Snowflakes with Turtle
# By Carrie Anne Philbin
# https://www.youtube.com/watch?v=DHmeX7YTHBY
