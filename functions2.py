import math
def periRectangle():
    l=float(raw_input("enter the length:-"))
    b=float(raw_input("enter the breadth:-"))
    print "The perimeter of this rectangle is:-",2*(l+b)

def periSquare():
    s=float(raw_input("enter the side:-"))
    print "The perimeter of this square is:-",s*4
def periCircle():
    r=float(raw_input("enter the radius:-"))
    print "The perimeter of this circle is:-",2*math.pi*r
def menu():
    print "MENU\nPerimeter of:-\n1.Rectangle\n2.Square\n3.Circle\n4.Exit"
    ch=int(raw_input("enter your choice:-"))
    return ch
while True:
    ch = menu()
    if ch==1:periRectangle()
    elif ch==2:periSquare()
    elif ch==3:periCircle()
    else:
        break