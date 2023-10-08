from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.player_1 = []
        self.making_player()

    def making_player(self):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.shapesize(0.5)
        turtle.goto(STARTING_POSITION)
        turtle.setheading(90)
        self.player_1.append(turtle)

    def moving_player(self):
        self.player_1[0].forward(MOVE_DISTANCE)

    def restarting_player(self):
        self.player_1[0].goto(STARTING_POSITION)
