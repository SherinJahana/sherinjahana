n=int(input("enter lim"))
for i in range(65,n+65):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print("\n")