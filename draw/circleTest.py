import turtle
t=turtle.Pen()
n=10
for i in range(5):

    t.setpos(-i*20,-i*20)
    n=n-1#n=n*(n-1)
    for x in range(4):
        t.forward(i*40)
        t.left(90)
turtle.done()