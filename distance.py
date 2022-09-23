import turtle

t=turtle.Turtle()

for j in range(2):
    for i in range(3):
        t.penup()
        t.pendown()
        t.dot(10)
        t.penup()
        t.forward(30)
    t.backward(30)
    t.right(90)
    t.forward(30)
    t.pendown()
    t.right(90)

    for i in range(3):
        t.penup()
        t.pendown()
        t.dot(10)
        t.penup()
        t.forward(30)
    t.backward(30)
    t.left(90)
    t.forward(30)
    t.left(90)