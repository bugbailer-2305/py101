runs=0
i=0
scorecard=[]
name=raw_input("enter player 1:-")
while True:
    abc=int(raw_input("enter the runs on  ball"+str(i+1)+":-"))
    scorecard.append(abc)
    if abc==0:
        print "oops you're out"
        break
    runs+=abc
    i+=1

print "total runs"+":-" +str(runs)
print "runs by "+str(name)
print scorecard