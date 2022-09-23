n=int(input("enter lim"))
for i in range(65,n):
    for j in range(65,(i+1)):
        print(chr(j),end=" ")
    print("\n")