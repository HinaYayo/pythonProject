import turtle
import random
t=turtle.Pen()
x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
t.penup()
t.setpos(x, y)
t.pendown()
turtle.done()

