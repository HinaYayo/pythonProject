import turtle
import random
t=turtle.Pen()
Colors=['red','green','blue','black']
for i in range(2):
    x=random.randrange(-turtle.window_width()//4,turtle.window_width()//4)
    y=random.randrange(-turtle.window_height()//4,turtle.window_height()//4)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for a in range(100):
        num = random.randint(0, 3)
        t.pencolor(Colors[num])
        t.circle(50)
        t.left(88)
turtle.done()

