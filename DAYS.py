a=["apr","jun","aug","oct","dec"]
b=["jan","mar","may","jul","sep","nov"]
c=["feb"]


month=input("enter the month")
year=int(input("enter the year"))

if month != 'feb':
    for i in a:
        if i==month:
            print("no of days = 30")
    for i in b:
        if i==month:   
            print("no of days = 31")
    

elif month=='feb':
    
    if year%4==0:
        print("leap year")
        print('no of days =29')
    else:
        print('no of days =28')    
else:
    print("enter a valid month")