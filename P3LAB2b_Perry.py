#START
import turtle
win = turtle.Screen()
t = turtle.Turtle()

#DISPLAY OPTIONS
t.pensize(3)
t.pencolor("blue")
t.shape("turtle")

#MOVE LOCATION FAR LEFT
t.penup()
t.left(270)
t.forward(100)
t.left(270)
t.forward(250)
t.left(270)
t.pendown()

#FIRST INITIAL:
t.forward(100)
t.left(220)
t.forward(60)
t.left(100)
t.forward(60)
t.left(220)
t.forward(100)

#MOVE LOCATION RIGHT
t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.pendown()

#SECOND INITIAL:
t.forward(100)
t.left(270)
t.forward(60)
t.left(270)
t.forward(40)
t.left(270)
t.forward(60)
t.left(90)
t.forward(50)

#MOVE DOWN
t.penup()
t.forward(100)


#END COMMANDS
win.mainloop()
