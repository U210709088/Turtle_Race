from turtle import *
from random import *
import turtle
import random
import time

setup(800,500)
title("TURTLE RACE")
bgcolor("#333333")
speed(0)

penup()
goto(-100,205)
color("white")
write("TURTLE RACE",font=("Arial",20,"bold"))
goto(235,200)
down()
right(90)
forward(450)



salmon_turtle=Turtle()
salmon_turtle.color("salmon")
salmon_turtle.shape("turtle")
salmon_turtle.shapesize(1.5)
salmon_turtle.penup()
salmon_turtle.goto(-300,150)
salmon_turtle.down()

green_turtle=Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300,50)
green_turtle.down()

yellow_turtle=Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300,-50)
yellow_turtle.down()

grey_turtle=Turtle()
grey_turtle.color("lightblue")
grey_turtle.shape("turtle")
grey_turtle.shapesize(1.5)
grey_turtle.penup()
grey_turtle.goto(-300,-150)
grey_turtle.down()

time.sleep(1)

while salmon_turtle.xcor() <= 230 and green_turtle.xcor() <=230 and yellow_turtle.xcor() <=230 and grey_turtle.xcor() <=230:
    salmon_turtle.forward(randint(1, 10))
    green_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))
    grey_turtle.forward(randint(1, 10))

if salmon_turtle.xcor()>green_turtle.xcor() and salmon_turtle.xcor()>yellow_turtle.xcor() and salmon_turtle.xcor()>grey_turtle.xcor():
    salmon_turtle.penup()
    salmon_turtle.goto(-150, -200)
    salmon_turtle.down()
    salmon_turtle.write("The Solmon Turtle Won!",font=("Arial",20,"bold"))
elif green_turtle.xcor()>salmon_turtle.xcor() and green_turtle.xcor()>yellow_turtle.xcor() and green_turtle.xcor()>grey_turtle.xcor():
    green_turtle.penup()
    green_turtle.goto(-150, -200)
    green_turtle.down()
    green_turtle.write("The Green Turtle Won!",font=("Arial",20,"bold"))
elif yellow_turtle.xcor()>salmon_turtle.xcor() and yellow_turtle.xcor()>green_turtle.xcor() and yellow_turtle.xcor()>grey_turtle.xcor():
    yellow_turtle.penup()
    yellow_turtle.goto(-150, -200)
    yellow_turtle.down()
    yellow_turtle.write("The Yellow Turtle Won!",font=("Arial",20,"bold"))
else :
    grey_turtle.penup()
    grey_turtle.goto(-150,-200)
    grey_turtle.down()
    grey_turtle.write("The Grey Turtle Won!",font=("Arial",20,"bold"))
exitonclick()

