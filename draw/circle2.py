import turtle as t#包含了t=turtle.Pen()
import random

t.colormode(255)
t.speed()
t.forward(1)
t.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
for i in range(0,10):#i:0~9
    #t.penup()
    n=10-i#10,9,8,7,6,5,4,3,2,1
    t.setpos(0, -n * 20)
    #.pendown()
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.begin_fill()
    t.circle(n * 20)
    t.end_fill()

t.done()