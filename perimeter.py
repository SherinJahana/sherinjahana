a=input("enter string")
s=[]
indexlist=[]
for i in a:
    c=0
    for J in a: 
        if i==J:
            c+=1
    if i not in s:
        s.append(i)
        indexlist.append(c)

for k in s:
    print(k,"present in ",indexlist[s.index(k)])        
p=indexlist.index(max(indexlist))        
print("most repeated is",s[p],"=",max(indexlist)) 