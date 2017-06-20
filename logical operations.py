"""n=int(raw_input("enter your number:-"))
if n%4==0:
    if n%5==0:
        print"correct"
    else :
        print "wrong"
else :
    print"wrong"
"""
'''
a=int(raw_input("enter your number:- \n"))
if a%4==0:
    print"correct"
elif a%5==0:
    print"correct"
else:
    print"wrong"
'''
m=int(raw_input("enter your number:-"))
if m%5==0 and m%4==0 and m%3==0:
    print m/5,m/4,m/3
else:
    print "not divisible"
