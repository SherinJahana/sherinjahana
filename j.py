for i in range(100,200):
    n=i
    sod=0
    while n>0:
        d=n%10
        sod=sod+d
        n=n/10
    if sod%2==0:
        print("sum of digit of ",i,"=",sod)