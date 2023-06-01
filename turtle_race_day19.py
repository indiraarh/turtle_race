from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter the color:")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# def name_obj(name, colour, a, b):
#     name = Turtle(shape="turtle")
#     name.color(colour)
#     name.penup()
#     name.goto(x=a, y=b)
#
# name_obj("tim", "red", -230, -100)
# name_obj("tom", "orange", -230, -60)
# name_obj("timmy", "yellow", -230, -20)
# name_obj("tommy", "green", -230, 20)
# name_obj("jim", "blue", -230, 60)
# name_obj("jimmy", "purple", -230, 100)

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} is the winner!")
            else:
                print(f"You've lost! The {winning_colour} is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
