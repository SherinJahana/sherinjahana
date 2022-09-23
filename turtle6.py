string=input("enter string")
v=['a','e','i','o','u']
string.lower()

for i in v:
    c=0
    for j in string: 
        if i==j:
            c+=1
    print(i,"present ",c,"times")