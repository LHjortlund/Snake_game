from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# TODO Create snake body
segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(x=-20, y=0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(x=-40, y=0)

# TODO  Move the snake
# TODO  Control the snake
# TODO  Detect collision with food
# TODO  Create a scoreboard
# TODO  Detect collision with wall
# TODO  Detect collision with tail

screen.exitonclick()