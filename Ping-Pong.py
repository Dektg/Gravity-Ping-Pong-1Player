import  turtle, random

window = turtle.Screen()
window.bgcolor('black')
window.setup(width=1.0, height=1.0)

border = turtle.Turtle()
border.color('white')
border.speed(0)
border.hideturtle()
border.up()
border.goto(-400, 300)
border.down()
border.begin_fill()
border.goto(400, 300)
border.goto(400, -300)
border.goto(-400, -300)
border.goto(-400, 300)
border.end_fill()

rand_Ball_Start_X = random.randint(-200, 200)

ball = turtle.Turtle()
ball.speed(0)
ball.up()
ball.goto(rand_Ball_Start_X, 250)
ball.shape("circle")
ball.color("black")

ball.speedY = -1
ball.speedX = -8



GRAVITY = 0.1

while True:
    ball.speedY = ball.speedY - GRAVITY
    ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
    if ball.ycor() <= -290:
        ball.speedY = -ball.speedY
    if ball.xcor() <= -390 or ball.xcor() >= 390:
        ball.speedX = -ball.speedX
window.mainloop()