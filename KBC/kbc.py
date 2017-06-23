import turtle as t
import time
t.bgpic('kbc1.png')
question = [
    {
        "question":"which is the most populer os?",
        "options":["a).linux","b).mac os","c).windows","d).none of these"],
        "ans":1
    },
    {
        "question":"which is the most popular computer company?",
        "options":["a).HP ","b).Dell","c).asus","d).Apple"],
        "ans":4
    }
]

t.bgcolor("dark blue")
score=0
def option(opt,x,y):
    t.speed(0)
    t.color("red")
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    t.lt(60)
    t.fd(50)
    t.lt(60)
    t.fd(50)
    t.lt(60)
    t.fd(250)
    t.lt(60)
    t.fd(50)
    t.lt(60)
    t.fd(50)
    t.lt(60)
    t.fd(250)
    t.end_fill()
    t.penup()
    t.color("white")
    t.setpos(x-260,y+20)
    t.write(opt,False,font=["jokerman",20,"bold"])

def show_question(ques):
    t.speed(0)
    margin=0
    w=t.window_width()
    ques_y=margin
    ques_x=0-10*len(ques)
    ques_color="white"
    ques_font=["jokerman",30,"bold"]
    t.penup()
    t.color(ques_color)
    t.setx(ques_x)
    t.sety(ques_y)
    t.pendown()
    t.write(ques,False,font=ques_font)

def create_opt(opt_list):
    w=t.window_width()
    opt_w=220
    x=(w/2-opt_w)/2.0
    option(opt_list[0],-x,-150)
    option(opt_list[1],x+opt_w,-150)
    option(opt_list[2],-x,-250)
    option(opt_list[3],x+opt_w,-250)

total_question=len(question)
score=0
ques_index=0

def display_question(q_index):
    show_question(question[q_index]["question"])
    create_opt(question[q_index]["options"])
    t.onscreenclick(get_option_index)

def get_option_index(x,y):
    t.speed(0)
    global score,ques_index
    if x<=-106 and x>=-548 and y>=-151 and y<=-66:
        option_clicked=1
    elif x>=38 and y>=-149 and x<=523 and y<=-66:
        option_clicked=2
    elif x>=-548 and x<=-106 and y<=-165 and y>=251:
        option_clicked=3
    elif x<=523 and x>=38 and y<=-165 and y>=-251:
        option_clicked=4

    if option_clicked==question[ques_index]["ans"]:
        t.color("yellow")
        t.clear()
        t.setpos(-150,0)
        score+=50
        t.write("right answer your score is:-"+str(score),False,font=["jokerman",30,"bold"])
        time.sleep(1.5)
        t.clear()
        ques_index+=1
        if ques_index==total_question:
            t.setpos(-550,0)
            t.write("you won the game CONGRATULATIONS!"+"score is:-"+str(score),False,font=["jokerman",30,"bold"])
            t.exitonclick()
        display_question(ques_index)
    else:
        t.clear()
        t.setpos(-150,0)
        t.color('yellow')
        t.write("oops!better luck next time!"+"your final score is:-"+str(score),False,font=["jokerman",30,"bold"])
        t.exitonclick()


t.speed(0)
display_question(ques_index)
t.mainloop()





