ch=input("enter operator")
while ch!='q':
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    if ch=='+':print("sum=",a+b)
    elif ch=='-':print("substraction=",a-b)
    elif ch=='*':print("product is =",a*b)
    elif ch=='/':print("division =",a/b)    
    else :
        print("wrong input")  
    ch=input("enter operator") 
    