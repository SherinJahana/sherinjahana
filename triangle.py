from cmath import sqrt


a=int(input("enter side a"))
b=int(input("enter side b"))
c=int(input("enter side c"))



if(a and b and c) <=0:print("a side must be greater 0 ")        

else:
    if (a==b==c):
        print("equlateral")
    elif (a==b or b==c or a==c) :
        print("isocles")
    else:
        print("scaline")
    s=(a+b+c)/2
    A=sqrt(s*(s-a)*(s-b)*(s-c))

    print("are is     =",A)
