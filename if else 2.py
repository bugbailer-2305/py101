print"Body Check"
print"1. Age"
print"2. Weight"
print"3. Height\n\n"

abc=int(raw_input("Enter your choice:-\n"))

if abc==1:
    age=int(raw_input("enter you age:-\n"))
    if age<13:
        print"you're a \n kid"
    elif age<18:
        if age>=13:
            print "you are a \n teenager"
    elif age<40:
        if age>18:
            print "you are \n young"
    elif age<60:
        if age>40:
            print "you are \n neutral"
    elif age<100:
        if age>60:
            print "you are  \n old"


elif abc==2:
    weight=int(raw_input("enter your weight:-\n"))
    if weight<=50:
        print "you are \n underweight"
    elif weight<=70:
        if weight>50:
            print "you are \n fit"
    elif weight<=100:
        if weight>70:
            print "you are \n overweight"
    else:
        print"you are obese"


elif abc==3:
    height=int(raw_input("enter your height:-"))
    print height/12,"feet"
    print height%12,"inches" 


