import turtle
t=turtle.Pen()
t.fillcolor('red')
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.circle(50)
t.end_fill()
turtle.done()