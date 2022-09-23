import math
n=int(input("enter no.of laddooos"))
s=int(input("no of laddos to be selected"))
print("no.of combinations can be created is = ",(math.factorial(n)))
for i in range (6,0,-1):
    for j in range(i,0,-1): print(j,end=" ") 
    print("\n")  