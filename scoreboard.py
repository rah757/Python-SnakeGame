from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.setposition(-50,250)
        self.hideturtle()
        self.pendown()
        self.write(f"Score: {self.score}", font = ("Arial", 20, "normal"))
        
    def increaseScore(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", font = ("Arial", 20, "normal"))
        
