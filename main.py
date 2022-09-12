#Unit_One_Project.py
# importing tool-turtle
import turtle

turtle.color("dark olive green")
# function to fill shape
turtle.begin_fill()

# creating first octogon using a loop
for x in range(8):
    turtle.fd(100)
    turtle.rt(45)

# function to end fill of shape
turtle.end_fill()

# moving "turtle" pen to make a new octogon
turtle.penup()
turtle.left(90)
turtle.fd(50)
turtle.pendown()
turtle.color("gold")

turtle.begin_fill()
# creating second octogon
for x in range(8):
    turtle.fd(20)
    turtle.rt(45)

turtle.end_fill()
# moving turtle with turtle.goto function
turtle.penup()
turtle.goto(90,100)
turtle.pendown()
turtle.color("tomato")
turtle.begin_fill()
# code for third octogon
for x in range (8):
    turtle.forward(30)
    turtle.right(45)

turtle.end_fill()


turtle.penup()
turtle.goto(-200,90)
turtle.pendown()
turtle.color("midnight blue")

turtle.begin_fill()
for x in range (8):
    turtle.fd(70)
    turtle.rt(45)

turtle.end_fill()

turtle.exitonclick()