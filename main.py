import random
from turtle import Turtle, Screen
import colorgram

my_screen = Screen()
james = Turtle()
my_screen.colormode(255)
james.penup()
james.speed("fastest")
james.hideturtle()

james.setheading(225)
james.forward(100)
james.setheading(0)

colours = colorgram.extract("image.jpg", 20)
x = 0
y = 0
for _ in range(10):
    james.sety(y)
    james.setx(x)
    y += 50
    for j in range(10):
        colour = random.choice(colours)
        james.dot(20, (colour.rgb.r, colour.rgb.g, colour.rgb.b))
        james.fd(50)

my_screen.exitonclick()
