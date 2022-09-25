import turtle
from turtle import Turtle,Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=500,height= 400)
user_bet=screen.textinput(title="make your bet", prompt="which turtle  will win the rate ? enter the color")
colors=["red", "orange", "yellow", "blue","purple","green"]
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]


for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-200, y=y_positions[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won! The {winning_color} turtle in winner")
            else:
                print(f"you've lose! The {winning_color} turtle in winner")
        rand_distance= random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()