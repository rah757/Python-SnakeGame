from turtle import Turtle

startPosition = [(0,0), (-20,0), (-40,0)]       # Modify as needed
movementSpeed = 20                              # Amount of px the snake segments move in each interval

class Snake:
    def __init__ (self):
        self.segments = []
        self.createSnake()
    
    def createSnake(self):
        for pos in startPosition:                   # Create snake
            newSegment = Turtle(shape='square')
            newSegment.color("white")
            newSegment.penup()
            newSegment.goto(pos)
            self.segments.append(newSegment)
            
    def moveSnake(self):
        for seg_num in range(len(self.segments)-1, 0, -1):       # this part is used to move the previous segment into the position of the newer segment
            new_x = self.segments[seg_num - 1].xcor()            # this part of the code moves the snake forward automatically 
            new_y = self.segments[seg_num - 1].ycor()            # it is done this way to ensure that the body of the snake follows the head properly
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(movementSpeed)