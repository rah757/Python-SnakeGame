from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

turtles = []

x = 0
y = 0

startPosition = [(0,0), (-20,0), (-40,0)]

segments = []


for pos in startPosition:
    newSegment = Turtle(shape='square')
    newSegment.color("white")
    newSegment.penup()
    newSegment.goto(pos)
    segments.append(newSegment)

screen.update()
    
gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):       # this part is used to move the previous segment into the position of the newer segment
        new_x = segments[seg_num - 1].xcor()            # this part of the code moves the snake forward automatically 
        new_y = segments[seg_num - 1].ycor()            # it is done this way to ensure that the body of the snake follows the head properly
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    






screen.exitonclick()