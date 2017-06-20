nhc = []
while True:
    print "Menu:-"
    print"1. Add an element"
    print"2. Add an element at a specific position"
    print"3. Extend the list"
    print"4. Print list"
    print"5. Exit"
    abc=int(raw_input("enter your number:-"))


    if abc==1:
        pqrs=raw_input("enter your element:-")
        nhc.append(pqrs)
    if abc==2:
        njk=raw_input("enter your element:-")
        nfja=int(raw_input("enter your position:-"))
        if nfja>len(nhc):
            print"invalid"
        else:
            nhc.insert(nfja-1,njk)
    if abc==3:
        n=[]
        k=int(raw_input("enter the no of elements:-"))
        for i in range(0,k):
            a=raw_input("enter your name"+str(i+1)+":-")
            n.append(a)
        nhc.extend(n)
    if abc==4:
        print nhc
    if abc==5:
        break

