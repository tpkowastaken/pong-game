#python code of pong made by tpko
#stole from freecodecamp.org
import turtle
import winsound
import time
barrier = False
lenght_num1 = 0
lenght_num2 = 0
lenght_num3 = 0
#info
print("pong 2.0")
print("by tpko")
#score
score_b = "0"
score_a = "0"

#names
p1paddle = 50
p2paddle = 50
name_a = input("hráč 1: ")
if name_a == "god_mode":
    p1paddle = 100
    lenght_num1 = 50
    print("god mode aktivován")
    winsound.PlaySound("sound/jtrovy_knedlik.wav", winsound.SND_ASYNC)
    name_a = input("teď sem dej tvoje jméno: ")
name_b = input("hráč 2: ")

if name_b == "god_mode":
    p2paddle = 100
    lenght_num2 = 50
    print("god mode aktivován")
    winsound.PlaySound("sound/jtrovy_knedlik.wav", winsound.SND_ASYNC)
    name_b = input("teď sem dej tvoje jméno: ")

#settings
p3paddle = 40
if input("možnos třetího hráče ano/ne: ") == "ano":
    barrier = True
    name_c = input("jméno třetího hráče: ")
    if name_c == "god_mode":
        print("god mode activated")
        winsound.PlaySound("sound/jtrovy_knedlik.wav", winsound.SND_ASYNC)
        lenght_num3 = 40
        p3paddle = 80
def score():
    score_limit = input("do kolika kol?: ")
    try:
        score_limit = int(score_limit)
        return score_limit
    except:
        print("napiš číslo!!")
        return score()
score_limit = score()
ball_spee = ""
def speed_input():
    try:
        ball_spee = input("rychlost 0.1-10 - normální je 1: ")
        ball_spee = float(ball_spee)
        return float(ball_spee)
    except:
        print("zadej číslo!")
        return speed_input()
ball_speed = speed_input()

print("ovládání:")
print("hráč 1: w, s")
print("hráč 2: šipka nahoru, šipka dolů")
print("hráč 3: t, g")

input("zmáčkni enter pro pokračování")
#speed

#window
win = turtle.Screen()
win.title("Pong od TPKO")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#bariéra 1
bar = turtle.Turtle()
bar.speed(0)
bar.shape("square")
bar.color("white")
bar.shapesize(stretch_wid=0.5, stretch_len=40)
bar.penup()
bar.goto(0, 300)
#bariéra 2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("white")
bar2.shapesize(stretch_wid=30, stretch_len=0.5)
bar2.penup()
bar2.goto(400, 0)
#bariéra 3
bar3 = turtle.Turtle()
bar3.speed(0)
bar3.shape("square")
bar3.color("white")
bar3.shapesize(stretch_wid=0.5, stretch_len=40)
bar3.penup()
bar3.goto(0, -300)
#bariéra 4
bar4 = turtle.Turtle()
bar4.speed(0)
bar4.shape("square")
bar4.color("white")
bar4.shapesize(stretch_wid=30, stretch_len=0.5)
bar4.penup()
bar4.goto(-400, 0)
#jenda čára

paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.penup()
paddle_one.goto(-350, 0)
if p1paddle == 100:
    paddle_one.shapesize(stretch_wid=10, stretch_len=1)
else:
    paddle_one.shapesize(stretch_wid=5, stretch_len=1)
#druhá čára

paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.penup()
paddle_two.goto(350, 0)
if p2paddle == 100:
    paddle_two.shapesize(stretch_wid=10, stretch_len=1)
else:
    paddle_two.shapesize(stretch_wid=5, stretch_len=1)
#třetí čára
if barrier == True:
    paddle_three = turtle.Turtle()
    paddle_three.speed(0)
    paddle_three.shape("square")
    paddle_three.color("white")
    paddle_three.penup()
    paddle_three.goto(0, 20)
    if p3paddle == 80:
        paddle_three.shapesize(stretch_wid=8, stretch_len=0.5)
    else:
        paddle_three.shapesize(stretch_wid=4, stretch_len=0.5)
#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = float(ball_speed)
ball.dy = float(ball_speed)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(name_a + ": " + score_a + "  " + name_b + ": "+ score_b, align = "center", font=("courier", 24, "normal"))
#functions
def puddle_one_up():
    if paddle_one.ycor() >= 250 - lenght_num1:
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_one.ycor()
        y += 20
        paddle_one.sety(y)
def puddle_one_down():
    if paddle_one.ycor() <= -225 + lenght_num1:
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_one.ycor()
        y -= 20
        paddle_one.sety(y)

def puddle_two_up():
    if paddle_two.ycor() >= 250 - lenght_num2:
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_two.ycor()
        y += 20
        paddle_two.sety(y)
def puddle_two_down():
    if paddle_two.ycor() <= -225 + int(lenght_num2):
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_two.ycor()
        y -= 20
        paddle_two.sety(y)
def puddle_three_down():
    if paddle_three.ycor() <= -225 + lenght_num3:
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_three.ycor()
        y -= 20
        paddle_three.sety(y)
def puddle_three_up():
    if paddle_three.ycor() >= 250 - lenght_num3:
        winsound.PlaySound("sound/block_sound.wav", winsound.SND_ASYNC)
    else:
        y = paddle_three.ycor()
        y += 20
        paddle_three.sety(y)
#keyboard binding
win.listen()
win.onkeypress(puddle_one_up, "w")
win.onkeypress(puddle_one_up, "W")

win.onkeypress(puddle_one_down, "s")
win.onkeypress(puddle_one_down, "S")

win.onkeypress(puddle_two_up, "Up")

win.onkeypress(puddle_two_down, "Down")

if barrier == True:
    win.onkeypress(puddle_three_down, "g")
    win.onkeypress(puddle_three_up, "t")
    win.onkeypress(puddle_three_down, "G")
    win.onkeypress(puddle_three_up, "T")
#main game loop
while True:
    win.update()

    #move the ball
    time.sleep(0.0075)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() <= -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() >= 380:
        ball.goto(0,0)
        ball.dx *= -1
        score_a = int(score_a) + 1
        pen.clear()
        pen.write(name_a + ": " + str(score_a) + "  " + name_b + ": " + str(score_b), align="center", font=("courier", 24, "normal"))
    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b = int(score_b) + 1
        pen.clear()
        pen.write(name_a + ": " + str(score_a) + "  " + name_b + ": " + str(score_b), align="center", font=("courier", 24, "normal"))
    #paddle
    if ball.xcor() >= 340 and ball.xcor()< 350 and ball.ycor() <= paddle_two.ycor() + int(p2paddle) and ball.ycor() >= paddle_two.ycor() - int(p2paddle):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() <= -340 and ball.xcor() >= -350 and ball.ycor() >= paddle_one.ycor() - int(p1paddle) and ball.ycor() <= paddle_one.ycor() + int(p1paddle):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
    if barrier == True:
        if ball.xcor() >= 0 and ball.xcor() <= 10 and ball.ycor() >= paddle_three.ycor() - int(p3paddle) and ball.ycor() <= paddle_three.ycor() + int(p3paddle):
            ball.setx(20)
            ball.dx *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
        if ball.xcor() <= 0 and ball.xcor() >= -10 and ball.ycor() >= paddle_three.ycor() - int(p3paddle) and ball.ycor() <= paddle_three.ycor() + int(p3paddle):
            ball.setx(-20)
            ball.dx *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
    if score_a == score_limit:
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("Hráč " + name_a + " vyhrál!", align="center",font=("courier", 50, "normal",))
        pen3 = turtle.Turtle()
        pen3.speed(0)
        pen3.color("white")
        pen3.penup()
        pen3.hideturtle()
        pen3.goto(0, -50)
        pen3.write("konec za 10", align="center", font=("courier", 20, "normal",))
        winsound.PlaySound("sound/end.wav", winsound.SND_ASYNC)
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 9", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 8", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 7", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 6", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 5", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 4", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 3", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 2", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 1", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        winsound.PlaySound("sound/bounce.wav", winsound.SND_APPLICATION)
        quit()
    if score_b == score_limit:
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("Hráč " + name_b + " vyhrál!", align="center",font=("courier", 50, "normal",))
        pen3 = turtle.Turtle()
        pen3.speed(0)
        pen3.color("white")
        pen3.penup()
        pen3.hideturtle()
        pen3.goto(0, -50)
        pen3.write("konec za 10", align="center", font=("courier", 20, "normal",))
        winsound.PlaySound("sound/end.wav", winsound.SND_ASYNC)
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 9", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 8", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 7", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 6", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 5", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 4", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 3", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 2", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        pen3.clear()
        pen3.write("konec za 1", align="center", font=("courier", 20, "normal",))
        time.sleep(1)
        winsound.PlaySound("sound/bounce.wav", winsound.SND_APPLICATION)
        quit()





