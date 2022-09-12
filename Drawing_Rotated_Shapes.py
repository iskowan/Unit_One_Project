import turtle

def makeASquare():
    for x in range(4):
        turtle.fd(100)
        turtle.rt(90)

for x in range(18):
    makeASquare()
    turtle.left(20)

turtle.speed(500)
turtle.exitonclick()