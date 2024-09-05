from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up") #90
screen.onkey(snake.down, "Down") #270
screen.onkey(snake.right, "Right") #0
screen.onkey(snake.left, "Left") #180

"""Moving snake forward"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

# Control the snake

# Create a scoreboard
#  Detect collision with wall
# Detect collision with tail

screen.exitonclick()