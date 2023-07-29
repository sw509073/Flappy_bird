
import turtle
import random
import os

win=turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("green")
win.bgpic("background.gif")
win.tracer(0)

score=0
lives=3
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.setposition(0,260)
pen.write("Score:0  Lives:3",align="center",font=("courier",24,"normal"))

win.register_shape("bird.gif")
win.register_shape("food.gif")
win.register_shape("poison.gif")

player=turtle.Turtle()
player.speed(0)
player.shape("bird.gif")
player.color("red")
player.penup()
player.setposition(0,-250)
player.direction="stop"

helpers=[]
for _ in range(20):
    helper=turtle.Turtle()
    helper.speed(0)
    helper.shape("food.gif")
    helper.color("blue")
    helper.penup()
    helper.setposition(-100,250)
    helper.speed=random.randint(2,5)
    helpers.append(helper)

killers=[]
for _ in range(30):
    killer=turtle.Turtle()
    killer.speed(0)
    killer.shape("poison.gif")
    killer.color("red")
    killer.penup()
    killer.setposition(100,250)
    killer.speed=random.randint(2,5)
    killers.append(killer)

def play_sound(sound_file,time=0):
    os.system("afplay {}&".format(sound_file))
    if time>0:
        turtle.ontimer(lambda:play_sound(sound_file,time),t=int(time*1000))
	

def player_right():
    player.direction="right"
        
def player_left():
    player.direction="left"

win.listen()
win.onkeypress(player_right,"Right")
win.onkeypress(player_left,"Left")

#play_sound("bgm.mp3",258)


while True:
    win.update()
    if player.direction=="left":
        x=player.xcor()
        x-=8
        player.setx(x)
    if player.direction=="right":
        x=player.xcor()
        x+=8
        player.setx(x)

    for helper in helpers:
        y= helper.ycor()
        y-=helper.speed
        helper.sety(y)

        if helper.distance(player)<40:
            play_sound("eat.wav")
            x=random.randint(-380,380)
            y=random.randint(350,400)
            helper.setposition(x,y)
            score+=10
            pen.clear()
            pen.write("Score:{}  Lives:{}".format(score,lives),align="center",font=("courier",24,"normal"))

        if helper.ycor()<-300:
            x=random.randint(-380,380)
            y=random.randint(350,400)
            helper.setposition(x,y)

    for killer in killers:
        y= killer.ycor()
        y-=killer.speed
        killer.sety(y)

        if killer.distance(player)<40:
            play_sound("lose.wav")
            x=random.randint(-380,380)
            y=random.randint(350,400)
            killer.setposition(x,y)
            score-=10
            lives-=1
            pen.clear()
            pen.write("Score:{}  Lives:{}".format(score,lives),align="center",font=("courier",24,"normal"))
            

        if killer.ycor()<-300:
            x=random.randint(-380,380)
            y=random.randint(350,400)
            killer.setposition(x,y)

    if lives<0:
        player.goto(10000,10000)
        helpers.clear()
        helper.hideturtle()
        killers.clear()
        killer.hideturtle()
        pen.clear()
        pen.goto(0,0)
        pen.write("Score:{}\nGAME OVER!".format(score),align="center",font=("courier",24,"normal"))
        break

win.mainloop()