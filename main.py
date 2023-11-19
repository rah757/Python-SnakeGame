from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

carl = Snake()

screen.update()
    
gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    carl.moveSnake()
    
    






screen.exitonclick()