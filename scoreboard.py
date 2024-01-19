from turtle import Turtle
font = "Arial"
fontsize = 20

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.readHighScore()
        self.penup()
        self.setposition(-50,250)
        self.hideturtle()
        self.pendown()
        self.updateScore()
        
    def readHighScore(self):
        with open("data.txt","r") as hs:
            self.high_score = int(hs.read())
    
    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", font = (font, fontsize))
    
    def increaseScore(self):
        self.score+=1
        self.updateScore()        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(str(self.score))
        self.score = 0
        self.updateScore()
        
    def gameOver(self):
        self.goto(-80,0)
        self.write("GAME OVER", font = (font,fontsize) )

