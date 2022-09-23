a=["jan","mar","may","july","sep","nov"]
b=["apr","june","aug","oct","dec"]
c=["feb"]
month=input("enter a month")
year=int(input("enter a year"))

if month!=c:
    for i in a:
        if i==month:
            print("31 days")
    for i in b:
        if i==month:
            print("30 days")
elif month=='feb':
    if year%4==0:
        print("29 days")
        print("leap yera")
    else:
        print("28 days")
else:
    print("enter a valid month")