side=int(input("enter number of sides"))
if side<3:
    print("no shapes can be created")
elif side == 3:
    print("triangle")
elif side == 4:
    print ("square or rectangle")
elif side==5:
    print("pentagon")
elif side==6:
    print("hexagon")
elif side==7:
    print("heptagon")
elif side==8:
    print("octagon")
elif side==9:
    print("nanogon")
elif side==10:
    print("pentagon")
else:
    print("side above ten")