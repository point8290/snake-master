from turtle import Turtle

SNAKE_DISTANCE = 20
INITIAL_SNAKE = 3

POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(INITIAL_SNAKE):
            self.add_segments(POSITION[i])

        self.head = self.segments[0]

    def add_segments(self, position):
        p = Turtle("square")
        p.penup()
        p.color("red")
        p.goto(position)
        self.segments.append(p)

    def tail_collision(self):
        for i in range(1, len(self.segments)):
            if self.segments[0].distance(self.segments[i]) < 10:
                return True

        return False

    def extend(self):
        position = self.segments[-1].pos()
        self.add_segments(position)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.head.forward(SNAKE_DISTANCE)

    def up(self):
        initial = self.head.heading()
        if initial == 0 or initial == 180:
            self.head.setheading(90)

    def down(self):
        initial = self.head.heading()
        if initial == 0 or initial == 180:
            self.head.setheading(270)

    def right(self):
        initial = self.head.heading()
        if initial == 90 or initial == 270:
            self.head.setheading(0)

    def left(self):
        initial = self.head.heading()
        if initial == 90 or initial == 270:
            self.head.setheading(180)

    def destroy(self):
        for snake in self.segments:
            snake.reset()
