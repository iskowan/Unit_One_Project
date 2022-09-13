# Unit_One_Project_S2.py
# by Anderson Iskowitz
import turtle

# setting speed of turtle
# turtle.speed(100)
# defining "makeAnOctogon" and "moveTurtle"
def makeAnOctogon(size, color):
    turtle.color(color)
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
makeAnOctogon(50, "dark sea green")
moveTurtle()

#octagon 2
makeAnOctogon(25, "orange red")
moveTurtle()

# octagon 3
makeAnOctogon(40, "royal blue")
moveTurtle()

# octagon 4
makeAnOctogon(30, "yellow green")
moveTurtle()

turtle.exitonclick()