import turtle
import time
import random
delay=0.1
wn= turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

head=turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,-100)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score 0")
segments=[]
score=0
highscore=0


def goup():
     if head.direction !="down":
          head.direction="up"

def godown():
     if   head.direction!="up":
          
          head.direction="down"

def goright():
     if   head.direction!="left":
          head.direction="right"

def goleft():
     if head.direction!="right":
          head.direction="left"
def move():
     if head.direction=="up":
          y=head.ycor()
          head.sety(y+20)
     if head.direction=="down":
          y=head.ycor()
          head.sety(y-20)
     if head.direction=="left":
          x=head.xcor()
          head.setx(x-20)
     if head.direction=="right":
          x=head.xcor()
          head.setx(x+20)
wn.listen()
wn.onkeypress(goup,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"a")
wn.onkeypress(goright,"d")
while True:
     wn.update()
     if head.distance(food)<20:
          x=random.randint(-290,290)
          y=random.randint(-290,290)
          food.goto(x,y)
          new_segment=turtle.Turtle()
          new_segment.speed(0)
          new_segment.shape("square")
          new_segment.color("black")
          new_segment.penup()
          segments.append(new_segment)
          score+=1
          if score>highscore:
              highscore=score
              pen.clear() 
              pen.write("score:{} High Score:{}".format(score,highscore))
          else:
               pen.clear() 
               pen.write("score:{} High Score:{}".format(score,highscore))
               
     for i in range(len(segments)-1,0,-1):
          x=segments[i-1].xcor()
          y=segments[i-1].ycor()
          segments[i].goto(x,y)
     if len(segments)>0:
          x=head.xcor()
          y=head.ycor()
          segments[0].goto(x,y)
     move()
     for k in segments:
          if k.distance(head)<20:
             time.sleep(1)
             head.goto(0,0)
             head.direction="stop"
             for j in segments:
                    j.goto(1000,1000)
             segments.clear()
     time.sleep(delay)
     if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
          time.sleep(1)
          head.goto(0,0)
          head.direction="stop"
          for j in segments:
               j.goto(1000,1000)
          segments.clear()
          pen.clear()
          score=0
          pen.write("score:{} High Score:{}".format(score,highscore))
wn.mainloop()

