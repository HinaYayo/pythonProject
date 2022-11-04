import random
import turtle
import random
t=turtle.Pen()
Colors=['red','green','blue','black']
for i in range(200):
   num=random.randint(0,3)
   t.pencolor(Colors[num])
   t.forward(i*2)
   t.left(88)
turtle.done()
