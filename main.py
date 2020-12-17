import time
from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food

# Screen functionality

screen = Screen()
screen.title("Snake Master")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Snake functionality
snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


def collision(head):
    if head.xcor() >= 290 or head.xcor() <= -290 or head.ycor() <= -290 or head.ycor() >= 290:
        return True
    return False


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score(game_on)
        snake.extend()

    if collision(snake.head) or snake.tail_collision():
        snake.destroy()
        game_on = False
        score.update_score(game_on)

screen.exitonclick()
