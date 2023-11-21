from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
from yum import Yum

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
yum = Yum()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.moveSnake()
    if snake.head.distance(food) < 15:      # Detect collision with food particle
        yum.clearYummy()    # clear the yum! writing before the next yum is written
        yum.yummy(snake.head.position())      # write yum! in places where food gets eaten
        food.respawnFood()
        score.increaseScore()
        snake.extendSnake()
        
    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False
        score.gameOver()
    



screen.exitonclick()