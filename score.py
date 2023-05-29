from turtle import Screen,Turtle


class ScoreDisplay(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        file = open('high_score.txt')
        con = file.read()
        print(type(con))
        self.high_score =int(con)
        file.close()
        self.penup()
        self.goto(0, 290)
        self.write(f"Score = {self.score}    HighScore ={self.high_score}", align="Center", font=('Arial', 20, "normal"))

        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Score = {self.score} , HighScore ={self.high_score}", align="Center", font=('Arial', 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="Center", font=('Arial', 24, "normal"))

    def reset_game(self):
        self.clear()
        self.score = 0
        file = open('high_score.txt', 'w')
        hs=str(self.high_score)
        file.write(hs)
        file.close()
        self.write(f"Score = {self.score}   HighScore ={self.high_score}", align="Center", font=('Arial', 20, "normal"))



