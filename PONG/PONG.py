import os
import turtle

wn = turtle.Screen()
wn.title("PONG by UPLAKSH")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# pong ball
pongball = turtle.Turtle()
pongball.speed(0)
pongball.shape("circle")
pongball.color("white")
pongball.penup()
pongball.goto(0, 0)
pongball.dx = 0.07
pongball.dy = 0.07

# panel_left
panel_left = turtle.Turtle()
panel_left.speed(0)
panel_left.shape("square")
panel_left.shapesize(stretch_wid=5, stretch_len=1)
panel_left.color("white")
panel_left.penup()
panel_left.goto(-350, 0)

# panel_right
panel_right = turtle.Turtle()
panel_right.speed(0)
panel_right.shape("square")
panel_right.shapesize(stretch_wid=5, stretch_len=1)
panel_right.color("white")
panel_right.penup()
panel_right.goto(350, 0)

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("PLAYER A:   PLAYER B:  ", align='center', font=("candara", 16, "bold"))


# functions
def panel_left_up():
    y = panel_left.ycor()
    y += 20
    if y > 250:
        y = 250
    panel_left.sety(y)


def panel_left_down():
    y = panel_left.ycor()
    y -= 20
    if y < -250:
        y = -250
    panel_left.sety(y)


def panel_right_up():
    y = panel_right.ycor()
    y += 20
    if y > 250:
        y = 250
    panel_right.sety(y)


def panel_right_down():
    y = panel_right.ycor()
    y -= 20
    if y < -250:
        y = -250
    panel_right.sety(y)


wn.listen()
wn.onkeypress(panel_left_up, 'w')
wn.onkeypress(panel_left_down, 's')
wn.onkeypress(panel_right_up, 'Up')
wn.onkeypress(panel_right_down, 'Down')

# main game loop
xscore = 0
yscore = 0
while True:
    wn.update()

    #     move the ball
    pongball.setx(pongball.xcor() + pongball.dx)
    pongball.sety(pongball.ycor() + pongball.dy)
    if pongball.ycor() > 290:
        pongball.sety(290)
        pongball.dy *= -1
        os.system('aplay border.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001
    if pongball.ycor() < -290:
        pongball.sety(-290)
        pongball.dy *= -1
        os.system('aplay border.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001
    if pongball.xcor() > 390:
        pongball.goto(0, 0)
        pongball.dx *= -1
        xscore += 1
        pen.clear()
        pen.write("PLAYER A: " + str(xscore) + " PLAYER B: " + str(yscore), align='center',
                  font=("candara", 16, "bold"))
        os.system('aplay miss.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001

    if pongball.xcor() < -390:
        pongball.goto(0, 0)
        pongball.dx *= -1
        yscore += 1
        pen.clear()
        pen.write("PLAYER A: " + str(xscore) + " PLAYER B: " + str(yscore), align='center',
                  font=("candara", 16, "bold"))
        os.system('aplay miss.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001
    if (340 < pongball.xcor() < 350) and (panel_right.ycor() + 50 > pongball.ycor() > panel_right.ycor() - 50):
        pongball.setx(340)
        pongball.dx *= -1
        os.system('aplay paddle.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001
    if (-350 < pongball.xcor() < -340) and (panel_left.ycor() + 50 > pongball.ycor() > panel_left.ycor() - 50):
        pongball.setx(-340)
        pongball.dx *= -1
        os.system('aplay paddle.wav&')
        pongball.dx += 0.001
        pongball.dy += 0.001
    if xscore == 10:
        pen.clear()
        pen.write("PLAYER A WON THE GAME ", align='center', font=("candara", 16, "bold"))
        pongball.goto(0, 0)
        pongball.dx *= 0
    elif yscore == 10:
        pen.clear()
        pen.write("PLAYER B WON THE GAME ", align='center', font=("candara", 16, "bold"))
        pongball.goto(0, 0)
        pongball.dx *= 0
