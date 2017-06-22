def areaRectangle():
    l=float(raw_input("enter the length:-"))
    b=float(raw_input("enter the breadth:-"))
    print "the area of this rectangle is:-",l*b
def areaSquare():
    s=float(raw_input("enter the side"))
    return s**2
def areaCircle():
    r=float(raw_input("enter the radius:-"))
    return 22/7*r**2
def menu():
    print "MENU:- \nArea of:-\n1.Circle\n2.Rectangle\n3.Square\n4 or more.Exit"


while True:
    menu()
    ch=int(raw_input("enter your choice:-"))
    if ch==1:print areaCircle()
    elif ch==2:areaRectangle()
    elif ch==3:print areaSquare()
    else:break