import turtle

# Set up the screen
win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("yellow")
win.bgpic(r"C:\Users\SathishkumarSuganesa\Documents\giphy.gif")

win.title("Ball Game")
win.tracer(0)

# Paddle and Ball Speeds
paddle_speed = 40
ball_speed = 0.2

# Scores
left_score = 0
right_score = 0

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(0, -380)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(0, 380)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

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

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

# Display winning message
def display_winner(winner):
    winner_message = turtle.Turtle()
    winner_message.speed(0)
    winner_message.color("green")
    winner_message.penup()
    winner_message.hideturtle()
    winner_message.goto(0, 0)
    winner_message.write(f"{winner} Wins!", align="center", font=("Courier", 36, "normal"))
    
 
    left_paddle.hideturtle()
    right_paddle.hideturtle()
    ball.hideturtle()


win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

# Main game loop
while True:
    win.update()

    if left_score >= 10:
        display_winner("Left Player")
        break
    elif right_score >= 10:
        display_winner("Right Player")
        break

  
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

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
        right_score += 1  
        update_score()

    if (ball.xcor() < -360 and ball.xcor() > -370) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")
        ball.dx *= -1
        left_score += 1 
        update_score()

   
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score -= 1  
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score -= 1  
        update_score()







  # # Center Paddle
# center_paddle = turtle.Turtle()
# center_paddle.speed(0)
# center_paddle.shape("square")
# center_paddle.color("white")
# center_paddle.shapesize(stretch_wid=5, stretch_len=1)
# center_paddle.penup()
# center_paddle.goto(0, 0)  
      



# def center_paddle_up():
#     y = center_paddle.ycor()
#     if y < 250: 
#         center_paddle.sety(y + paddle_speed)

# def center_paddle_down():
#     y = center_paddle.ycor()
#     if y > -250: 
#         center_paddle.sety(y - paddle_speed)

# win.onkeypress(center_paddle_up, 'f')  
# win.onkeypress(center_paddle_down, 'g') 
