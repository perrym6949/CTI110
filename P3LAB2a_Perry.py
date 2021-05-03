#START
import turtle
win = turtle.Screen()
t = turtle.Turtle()

#DISPLAY OPTIONS
t.pensize(4)
t.pencolor("red")
t.shape("turtle")

#SQUARE LOOP
for i in range(4):
    t.forward(100)
    t.left(90)

#MOVE TURTLE ABOVE SQUARE
t.penup()
t.left(90)
t.forward(250)
t.left(90)
t.pendown()

t.color("blue")

#TRIANGLE LOOP
for i in range(3):
    t.left(120)
    t.forward(100)
    t.left(120)

#MOVE TURTLE
t.penup()
t.forward(200)
t.left(90)
t.pendown()

t.color("green")

#SQUARE LOOP
for i in range(4):
    t.forward(100)
    t.left(90)

#MOVE TURTLE
t.penup()
t.forward(300)
t.left(120)
t.forward(100)
t.pendown()

t.color("magenta")

#TRIANGLE LOOP
for i in range(3):
    t.left(120)
    t.forward(100)
    t.left(120)


#END COMMANDS
win.mainloop()
