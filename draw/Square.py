import turtle as t#包含了t=turtle.Pen()
import random

t.hideturtle()#隐藏画笔
t.colormode(255)
t.speed()

for i in range(1,5):
    n=5-i
    t.penup()
    t.goto(-n*20, -n * 20)
    t.pendown()
    t.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill()
    for x in range(4):
        t.forward(n*40)
        t.left(90)
    t.end_fill()
t.done()