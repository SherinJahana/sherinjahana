import turtle

t=turtle.Turtle()
t.speed(10)
for i in range(72):
    t.right(30)
    t.forward(50)
    t.right(30)
    t.forward(50)
    t.left(30)
    t.forward(50)


    t.penup()
    t.backward(50)
    t.right(30)
    t.backward(50)
    t.left(30)
    t.backward(50)
    t.pendown()
    t.right(5)