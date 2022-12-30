# using turtle module
import turtle
wn = turtle.Screen()
wn.title("Pong by @CalvinPark")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=2
ball.dy=2

# paddle_a_up Function
def paddle_a_up():
    # it returns the y coordinate
    y = paddle_a.ycor()
    # add 20 to y pixel
    y += 20
    paddle_a.sety(y)

# paddle_a_down Function
def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

# paddle_b_up Function
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# paddle_b_down Function
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
# when the user press "w" then paddle goes up
wn.onkeypress(paddle_a_up,"w")

# when the user press "s" then paddle goes down
wn.onkeypress(paddle_a_down, "s")

# when the user press "Up" then paddle b goes up
wn.onkeypress(paddle_b_up, "Up")

# when the user press "Down" then paddle b goes up
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    