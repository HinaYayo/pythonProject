import turtle
t=turtle.Pen()
colors=['yellow','green','blue','red']
for i in range(100):
    t.pencolor(colors[i%4])
    t.circle(i*2)
turtle.done()