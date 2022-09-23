print("","-"*30,"\n|  1 - addition \n|  2 - sbstraction \n|  3 - multiplication \n|  4 - division \n|  q - quit\n","-"*30)
ch=input("enter a operator")
while ch!="q" and ch!="Q":
    a=float(input("enter a number"))
    b=float(input("enter a number"))
    if ch=="1" or ch=="add": print(a,"+",b,"=",a+b)
    elif ch=="2" or ch=="sub": print(a,"-",b,"=",a-b)
    elif ch=="3" or ch=="mul": print(a,"*",b,"=",a*b)
    elif ch=="4" or ch=="div": print(a,"/",b,"=",a/b)
    else:
        print("wrong input")
    print("-"*30,"\n|  1 - addition \n|  2 - substraction \n|  3 - multiplication \n|  4 - division \n|  q - quit\n","-"*30)
    ch=input("enter a operator")