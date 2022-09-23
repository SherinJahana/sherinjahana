import math
n=int(input("enter no.of laddooos"))
s=int(input("no of laddos to be selected"))
print("no.of combinations can be created is = ",(math.factorial(n))/math.factorial(n-s))