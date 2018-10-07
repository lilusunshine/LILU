import turtle

def mygoto(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def pentagram(x):
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(x)
        turtle.right(144)
    turtle.end_fill()

turtle.setup(600,400,0,0)
turtle.color("yellow")
turtle.bgcolor("red")
turtle.fillcolor("yellow")

mygoto(-250,95)
pentagram(100)

for i in range(4):
    x=1
    if i in [0,3]:
        x=0
    mygoto(-120+x*30,150-i*40)
    turtle.left(15-i*15)
    pentagram(30)

turtle.done()
