import turtle
turtle.Screen().bgcolor
turtle.Screen().setup(400,500)
square=turtle.Turtle()

num_sides=4
side_length=100
angle=360.0/num_sides

for i in range(num_sides):
    square.fd(side_length)
    square.left(angle)

turtle.done()