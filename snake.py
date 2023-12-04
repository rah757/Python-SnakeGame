from turtle import Turtle

startPosition = [(0,0), (-20,0), (-40,0)]       # Modify as needed
movementSpeed = 20                              # Amount of px the snake segments move in each interval
down = 270              # setting angles for the snake heading
left = 180
up = 90
right = 0

class Snake:
    def __init__ (self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]           # Head of the snake is kept as a separate variable so it can be reused a lot in code
    
    def createSnake(self):
        for pos in startPosition:                   # Create snake
            self.addSegment(pos)
            
    def moveSnake(self):
        for seg_num in range(len(self.segments)-1, 0, -1):       # this part is used to move the previous segment into the position of the newer segment
            new_x = self.segments[seg_num - 1].xcor()            # this part of the code moves the snake forward automatically 
            new_y = self.segments[seg_num - 1].ycor()            # it is done this way to ensure that the body of the snake follows the head properly
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(movementSpeed)
    
    def addSegment(self, position):
        newSegment = Turtle(shape='square')
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]  
    
    def extendSnake(self):
        # add new segment to snek
        self.addSegment(self.segments[-1].position())
        
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)