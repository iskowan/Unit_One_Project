# Unit_One_Project_S2.py
# by Anderson Iskowitz
import turtle

# setting speed of turtle
# turtle.speed(100)
# defining "makeAnOctogon" and "moveTurtle"
def makeAnOctogon(size):
    turtle.begin_fill()
    for x in range(8):
        turtle.fd(size)
        turtle.right(45)
    turtle.end_fill()

def moveTurtle():
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()


# octagon 1
turtle.color("dark sea green")
makeAnOctogon(50)
moveTurtle()
#octagon 2
turtle.color("orange red")
makeAnOctogon(25)
moveTurtle()
# octagon 3
turtle.color("royal blue")
makeAnOctogon(40)
moveTurtle()
# octagon 4
turtle.color("yellow green")
makeAnOctogon(30)
moveTurtle()

turtle.exitonclick()