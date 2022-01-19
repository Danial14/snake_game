import time
from turtle import Turtle, Screen
screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segMents = []
        self.snakeSetup()
        self.snakeHead = self.snake_segMents[0]

    def snakeSetup(self):
        x_axis = 0
        for _ in range(0, 3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setposition(x=x_axis, y=0)
            x_axis = x_axis - 20
            self.snake_segMents.append(snake)

    def changePosition(self, angle):
        self.snakeHead.setheading(angle)
        self.move()
    def moveUp(self):
        if self.snakeHead.heading() != DOWN and self.snakeHead.heading() != UP:
            self.changePosition(UP)

    def moveDown(self):
        if self.snakeHead.heading() != UP and self.snakeHead.heading() != DOWN:
            self.changePosition(DOWN)

    def moveRight(self):
        if self.snakeHead.heading() != LEFT and self.snakeHead.heading() != RIGHT:
            self.changePosition(RIGHT)

    def moveLeft(self):
        if self.snakeHead.heading() != RIGHT and self.snakeHead.heading() != LEFT:
            self.changePosition(LEFT)

    def move(self):
        for i in range(2, 0, -1):
            snakeBodyPart = self.snake_segMents[i]
            snakeBodyPart.goto(self.snake_segMents[i - 1].position())
        self.snakeHead.forward(10)

    def detectFoodCollision(self, food):
        return self.snakeHead.distance(food) < 15

    def detectWallCollision(self):
        return self.snakeHead.xcor() == 290 or self.snakeHead.xcor() == -290 or self.snakeHead.ycor() == 290 or self.snakeHead.ycor() == -290