from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.15)
    snake.moveSnake()
    if snake.head.distance(food) < 15:      # Detect collision with food particle
        print("Yummmmmmmm")
        food.respawnFood()
    






screen.exitonclick()