from turtle import Turtle

font = "Arial"
fontsize = 20

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.setposition(-50,250)
        self.hideturtle()
        self.pendown()
        self.updateScore()
        
    def updateScore(self):
        self.write(f"Score: {self.score}", font = (font, fontsize))
    
    def increaseScore(self):
        self.clear()
        self.score+=1
        self.updateScore()        
        
    def gameOver(self):
        self.goto(-80,0)
        self.write("GAME OVER", font = (font,fontsize) )

