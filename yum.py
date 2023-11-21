from turtle import Turtle

class Yum(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
    def yummy(self, pos):
        self.setposition(pos)
        self.pendown()
        self.write(f"Yum!", font = ("Arial", 10, "normal"))
        self.penup()
        
    def clearYummy(self):
        self.clear()
        
        