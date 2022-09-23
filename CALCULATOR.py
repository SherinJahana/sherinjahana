a=input("enter string")
m=input("enter searching element")
s=[]
c=0
c1=-1
for j in a:
    c1+=1
    if j==m:
        s.append(c1)
        c+=1
if c%2==0:print("no center element or it is a even number repeatation")
else:
    im=int((c/2))
    print("the index value of middle=",s[im])
print(s)