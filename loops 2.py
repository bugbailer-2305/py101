abc=int(raw_input("enter your number:-"))

if abc%5==0 and abc%3==0:
    for i in range(1,31):
        print i*abc
elif abc%3==0:
    for i in range(1,11):
        print i*abc
elif abc%5==0:
    for i in range(1,21):
        print i*abc
elif abc%5==0 and abc%3==0:
    for i in range(1,31):
        print i*abc