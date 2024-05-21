import random
from turtle import Turtle, Screen

# Variables
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
NUMBER_OF_TURTLES = 6
screen = Screen()


def create_screen():
    screen.setup(width=500, height=400)
    return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color "
                                                          "(red, orange, yellow, green, blue, violet):")


def check_user_input(input_color):
    if input_color not in colors:
        new_input = screen.textinput(title="Wrong color!", prompt="Which turtle will win the race? Enter a color "
                                                                  "(red, orange, yellow, green, blue, violet):")
        check_user_input(new_input)


def create_turtles():
    temp_y = -100
    for turtle_index in range(0, NUMBER_OF_TURTLES):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(colors[turtle_index])
        turtle.goto(x=-230, y=temp_y)
        temp_y += 45
        turtles.append(turtle)


def start_race(bet_color):
    is_winner = False
    while not is_winner:
        for turtle in turtles:
            turtle.forward(distance=random.random()*5)
            if turtle.xcor() > 210:
                is_winner = True
                if turtle.pencolor() == bet_color:
                    print("You won!")
                else:
                    print(f"You lost! The {turtle.pencolor()} turtle won!")


if __name__ == '__main__':
    # Create the screen
    user_bet = create_screen()

    # Check the user input
    check_user_input(user_bet)

    # Create the turtles
    create_turtles()

    # Start race
    start_race(user_bet)

    screen.exitonclick()
