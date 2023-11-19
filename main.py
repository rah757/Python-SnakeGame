from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("Snake game")

turtles = []

x = 0
y = 0

startPosition = [(0,0), (-20,0), (-40,0)]


for pos in startPosition:
    carl = Turtle(shape='square')
    carl.color("white")
    carl.goto(pos)









screen.exitonclick()