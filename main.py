from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

"""Moving snake forward"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




# TODO  Control the snake
# TODO  Detect collision with food
# TODO  Create a scoreboard
# TODO  Detect collision with wall
# TODO  Detect collision with tail

screen.exitonclick()