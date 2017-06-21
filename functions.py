while True:
    print "MENU"
    print "Area Of:-"
    print "1. circle"
    print "2. square"
    print "3.rectangle"
    print "4. exit"
    abc=int(raw_input("enter your option:-"))
    if abc==1:
        radius=float(raw_input("enter the radius:-"))
        arcircle=22/7*radius**2
        print arcircle
    elif abc==2:
        s=float(raw_input("enter the side:-"))
        arsquare=s**2
        print arsquare
    elif abc==3:
        l=float(raw_input("enter the length"))
        b=float(raw_input("enter the breadth"))
        arrec=2*(l+b)
        print arrec
    elif abc==4:
        break