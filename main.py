# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Turtle, Screen
import time, Snake
from food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake = Snake.Snake()

screen.onkey(key="Up", fun=snake.moveUp)
screen.onkey(key="Down", fun=snake.moveDown)
screen.onkey(key="Right", fun=snake.moveRight)
screen.onkey(key="Left", fun=snake.moveLeft)
screen.listen()
gameIsOn = True
food = Food()
snakeHead = snake.snakeHead
score = Scoreboard()
while gameIsOn:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.detectFoodCollision(food= food):
        food.refresh()
        score.updateScore()
        snake.addBodySegment()
    if snake.detectWallCollision():
        score.gameOver()
        gameIsOn = False
    if snake.detectBodyCollision():
        score.gameOver()
        gameIsOn = False

screen.exitonclick()

