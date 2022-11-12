import random
import turtle
t=turtle.Pen()
Colors=['red','green','blue','black']
for i in range(360):
   num=random.randint(0,3)
   t.pencolor(Colors[num])
   t.forward(1)
   t.left(1)
turtle.done()
