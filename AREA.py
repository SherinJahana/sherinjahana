string=input("enter the string")
balaned=0
str_count=0
for i in string:
    if i=="a" or i=='A':
        str_count+=1
    if i=="j" or i=='J':
        str_count-=1
    if str_count==0:
        balaned+=1
print("no of balanced string is ",balaned)