'''
players=int(raw_input("enter the number of players:-"))
a={}
for i in range(0,players):
    name=raw_input("enter players name:-")
    ball=1
    totalruns=0
    scorecard=[]
    while True:
        runs=int(raw_input("enter runs on ball "+str(ball)+":-"))
        ball+=1
        totalruns+=runs
        scorecard.append(runs)
        if runs==0:
            print name +" you are out"
            print "total runs by "+name+":-"+"\n"+str(totalruns)
            print scorecard
            a[name]=totalruns
            break

print a
'''



