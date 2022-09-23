prices=[]
c=0

for i in range(4):
    price=int(input("enter price"))
    
    prices.append(price)
    c+=1
def price_to_pay(p2):
    p=p2
    b1=max(p)
    p.remove(b1)
    b2=max(p)
    b=b1+b2
    return(b)
    
def find_least_prices(p1):
    p=p1
    s1=min(p)
    p.remove(s1)
    s2=min(p)
    l=s1+s2
    return(l)

lp=find_least_prices(prices)
print("least price=",lp)
pp=price_to_pay(prices)
print("price to pay=",pp)