#Unit_One_Project.py
# importing tool-turtle
import turtle

# creating first octogon using a loop
for x in range(8):
    turtle.fd(100)
    turtle.rt(45)

# moving "turtle" pen to make a new octogon
turtle.penup()
turtle.left(90)
turtle.fd(50)
turtle.pendown()

# creating second octogon
for x in range(8):
    turtle.fd(20)
    turtle.rt(45)

# moving turtle with turtle.goto function
turtle.penup()
turtle.goto(90,100)
turtle.pendown()
# code for third octogon
for x in range (8):
    turtle.forward(30)
    turtle.right(45)

turtle.penup()
turtle.goto(-200,90)
turtle.pendown()

for x in range (8):
    turtle.fd(70)
    turtle.rt(45)


turtle.exitonclick()