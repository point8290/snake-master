from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.font = ("Courier", 15, "normal")
        self.cur_score = 0
        self.str = f"SCORE : {self.cur_score}"
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(self.str, align="center", font=self.font)

    def update_score(self, game_on):
        if game_on:
            self.clear()
            self.cur_score += 1
            self.str = f"SCORE : {self.cur_score}"
            self.write(self.str, align="center", font=self.font)
        else:
            self.clear()
            self.goto(0, 0)
            self.str = f" GAME OVER\nYOUR SCORE: {self.cur_score}"
            self.write(self.str, align="center", font=self.font)
