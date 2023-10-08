from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.hideturtle()

    def increasing_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def game_over(self):
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game over  !!! ", align="center", font=FONT)
        self.hideturtle()
