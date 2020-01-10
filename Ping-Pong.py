import  turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(width=1.0, height=1.0)

border = turtle.Turtle()
border.color('white')
border.pensize(5)
border.hideturtle()
border.up()
border.goto(-300, 300)
border.down()
border.begin_fill()
border.goto(300, 300)
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.end_fill()

ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.up()


window.mainloop()