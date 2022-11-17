import turtle as t#包含了t=turtle.Pen()
import random

t.hideturtle()#隐藏画笔
t.colormode(255)
t.speed()

for i in range(1,5):
    t.penup()
    t.goto(-i*20, -i * 20)
    t.pendown()
    t.color(random.randint(0,256),random.randint(0,256),random.randint(0,256))
    #t.fillcolor('red')
    #t.begin_fill()
    for x in range(4):
        t.forward(i*40)
        t.left(90)
    #t.end_fill()
t.done()