# python pong game

import turtle

# Window parameters
wn = turtle.Screen()
wn.title("Pong by Sam")
wn.bgcolor("grey")
wn.setup(width=900, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(390, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.66
ball.dy = -0.66

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Italic", 21, "normal"))

# Score
score_a = 0
score_b = 0


# Functions, moving of paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 21
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 21
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 21
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 21
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 430:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Italic", 21, "normal"))

    if ball.xcor() < -430:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Italic", 21, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 380 and ball.xcor() < 390) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(380)
        ball.dx *= -1

    if (ball.xcor() < -380 and ball.xcor() > -390) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-380)
        ball.dx *= -1