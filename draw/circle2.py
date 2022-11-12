import turtle as t#包含了t=turtle.Pen()
import random

t.colormode(255)
t.speed()
t.forward(1)

for i in range(1,10):
    t.penup()
    t.goto(0, -i * 20)
    t.pendown()
    #t.pencolor(255,255,255)
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #t.circle(i * 20)
    for x in range(4):
        t.forward(100)
        t.left(90)
t.done()