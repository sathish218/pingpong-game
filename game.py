import turtle

# Set up the screen
win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("yellow")
win.title("Ball Game")
win.tracer(0) 

# Paddle speed
paddle_speed = 40  

# Ball speed
ball_speed = 0.2 

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed 
ball.dy = ball_speed  

# Paddle movement functions
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250: 
        left_paddle.sety(y + paddle_speed)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240: 
        left_paddle.sety(y - paddle_speed)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250: 
        right_paddle.sety(y + paddle_speed)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240: 
        right_paddle.sety(y - paddle_speed)

# Keyboard bindings
win.listen()
win.onkeypress(left_paddle_up, 'w')    
win.onkeypress(left_paddle_down, 's') 
win.onkeypress(right_paddle_up, 'Up')   
win.onkeypress(right_paddle_down, 'Down') 

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball collision with paddles
    if (ball.xcor() > 360 and ball.xcor() < 370) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue") 
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red") 
        ball.dx *= -1

    # Ball out of bounds (left and right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
