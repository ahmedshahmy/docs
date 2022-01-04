import turtle
import math
import random

t=turtle.Turtle()
sc=turtle.Screen()

turtle.bgcolor("black")
t.color("green")

t.speed(3)
t.width(2)

def head(x,y):
    t.setpos(x,y)
    t.goto(x,y)

def up():
    t.setheading(90)
    t.fd(5)
    

def down():
    t.setheading(270)
    t.fd(5)
def left():
    t.setheading(180)
    t.fd(5)
def right():
    t.setheading(0)
    t.fd(5)





sc.listen()

sc.onkeypress(up,"Up")
sc.onkeypress(left,"Left")
sc.onkeypress(right,"Right")
sc.onkeypress(down,"Down")

sc.onscreenclick(head)




# for i in range(200):
#     t.forward(i)
#     t.left(i)

sc.mainloop()