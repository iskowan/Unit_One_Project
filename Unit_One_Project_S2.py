# Unit_One_Project_S2.py
# by Anderson Iskowitz
import turtle

# setting speed of turtle
turtle.speed(100)
# defining "makeAnOctogon" and "moveTurtle"
def makeAnOctogon(size):
    for x in range(8):
        turtle.fd(size)
        turtle.rt(45)

def moveTurtle():
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

# begining of code

# octagon 1
turtle.color("dark sea green")
turtle.begin_fill()
makeAnOctogon(50)
turtle.end_fill()
moveTurtle()
#octagon 2
turtle.color("orange red")
turtle.begin_fill()
makeAnOctogon(25)
turtle.end_fill()
moveTurtle()
# octagon 3
turtle.color("royal blue")
turtle.begin_fill()
makeAnOctogon(40)
turtle.end_fill()
moveTurtle()
# octagon 4
turtle.color("yellow green")
turtle.begin_fill()
makeAnOctogon(30)
turtle.end_fill()
moveTurtle()

turtle.exitonclick()