# Unit_One_Project_S2.py
# by Anderson Iskowitz
import turtle

# setting speed of turtle
# turtle.speed(100)
# defining "makeAnOctogon" and "moveTurtle"
def moveTurtle():
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

def makeAnOctogon(size, color):
    turtle.color(color)
    turtle.begin_fill()
        turtle.fd(size)
    for x in range(8):
        turtle.right(45)
    turtle.end_fill()
    moveTurtle()


# octagon 1
makeAnOctogon(50, "dark sea green")

#octagon 2
makeAnOctogon(25, "orange red")

# octagon 3
makeAnOctogon(40, "royal blue")

# octagon 4
makeAnOctogon(30, "yellow green")


turtle.exitonclick()