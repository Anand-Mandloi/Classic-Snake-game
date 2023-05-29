from turtle import Screen
from snake import Snake
from score import ScoreDisplay

import time
import food


screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=650, height=650)
screen.bgcolor("grey")

snake = Snake()
food = food.Food()
score_disp = ScoreDisplay()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

Game = True

while Game:
    screen.update()
    snake.move_snake(20)

    if snake.head.distance(food) < 20:
        food.refresh()
        score_disp.update_score()
        snake.add_segment()

    if snake.head.xcor() >= 320 or snake.head.xcor() <= -320 or snake.head.ycor() >= 320 or snake.head.ycor() <= -320:
        snake.reset_game()
        score_disp.reset_game()

    if snake.collision_with_tail():
        snake.reset_game()
        score_disp.reset_game()
    time.sleep(0.1)

screen.exitonclick()
