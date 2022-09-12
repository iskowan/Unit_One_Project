import turtle

# defining "makeAnOctogon" and "moveTurtle"
def makeAnOctogon():
    for x in range(8):
        turtle.fd(50)
        turtle.rt(45)

def moveTurtle():
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

# begining of code

turtle.color("dark olive green")
turtle.begin_fill()
makeAnOctogon()
turtle.end_fill()
moveTurtle()
turtle.color("red")
turtle.begin_fill()
makeAnOctogon()
turtle.end_fill()
moveTurtle()
turtle.color("blue")
turtle.begin_fill()
makeAnOctogon()
turtle.end_fill()
moveTurtle()
turtle.color("yellow")
turtle.begin_fill()
makeAnOctogon()
turtle.end_fill()
moveTurtle()
