import turtle


t=turtle.Turtle()
t.speed(10)
for i in range(0,11):
    xf=0
    yf=(10-i)*20
    xt=i*20
    yt=0

    t.penup()
    t.goto(xf,yf)
    t.pendown()
    t.goto(xt,yt)

for i in range(0,10):
    xf=-1
    yf=-(10-i)*20
    xt=i*20
    yt=-1

    t.penup()
    t.goto(xf,yf)
    t.pendown()
    t.goto(xt,yt)

for i in range(-10,0,1):
    xf=-1
    yf=(10+i)*20
    xt=i*20
    yt=-1

    t.penup()
    t.goto(xf,yf)
    t.pendown()
    t.goto(xt,yt)

for i in range(-10,0,1):
    xf=-1
    yf=-(10+i)*20
    xt=i*20
    yt=-1

    t.penup()
    t.goto(xf,yf)
    t.pendown()
    t.goto(xt,yt)