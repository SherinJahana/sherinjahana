a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))

if a>b and a>c and a>d:
    print("biggest is",a)
elif b>c and b>d:
    print("biggest is ", b)
elif c>d:
    print("biggest is ", c)
else:
    print("biggest is",d)