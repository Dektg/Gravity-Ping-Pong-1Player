import  turtle, random

window = turtle.Screen()
window.bgcolor('black')
window.setup(width=1.0, height=1.0)
window.tracer(2)

space_rocket = 80

score = 0

FONT = ("Arial", 44)
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(0, 300)
s1.write(score, font=FONT)

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
ball.speedX = random.choice([-4,-3,-2, 2, 3,4])

# РАКЕТКА
rocket = turtle.Turtle()
rocket.color("black")
rocket.shape("square")
rocket.shapesize(stretch_len=5, stretch_wid=1)
    # Не оставляет следов
rocket.penup()
rocket.goto(0, -250)

# УПРАВЛЕНИЕ РАКЕТКИ
def move_Right():
    x = rocket.xcor() + space_rocket
    if x > 350:
        x = 350
    rocket.setx(x)


def move_Left():
    x = rocket.xcor() - space_rocket
    if x < -350:
        x = -350
    rocket.setx(x)


window.listen()
window.onkeypress(move_Right, "d")
window.onkeypress(move_Left, "a")
window.onkeypress(move_Right, "Right")
window.onkeypress(move_Left, "Left")


GRAVITY = 0.07

while True:
    if ball.ycor() >= rocket.ycor() - 10 and ball.ycor() <= rocket.ycor() + 10 \
            and ball.xcor() >= rocket.xcor() - 50 and ball.xcor() <= rocket.xcor() + 50:
        ball.speedY = -ball.speedY
        score += 1
        s1.clear()
        s1.write(score, font=FONT)

    ball.speedY = ball.speedY - GRAVITY
    ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
    if ball.ycor() <= -290:
        ball.goto(rand_Ball_Start_X, 250)
        ball.speedY = -1
        score -= 1
        s1.clear()
        s1.write(score, font=FONT)

    if ball.xcor() <= -390 or ball.xcor() >= 390:
        ball.speedX = -ball.speedX
window.mainloop()