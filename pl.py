a=input("enter string")
'''s=[]
r=[]
c=0
for i in a:
    c+=1
    s.append(i)
for j in range(c+1,0,-1):r.append(s[j])
print(r)
  '''
# b=a[::-1]
b=''.join(reversed(a))
if a==b:print(a,"is palindrome")
else:print(a,"is not palindrome")
