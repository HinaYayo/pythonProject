import turtle as t
import random
t.hideturtle()
t.colormode(255)
t.speed(0)
for i in range(10):
    t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    n=10-i
    t.penup()
    t.goto(0,-20*n)
    t.pendown()
    t.begin_fill()
    t.circle(20*n)
    t.end_fill()
t.done()