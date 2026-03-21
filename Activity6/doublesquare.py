import turtle
turtle.Screen().bgcolor("Aqua")
board=turtle.Turtle()

for i in range(4):
    board.fd(100)
    board.left(90)

board.penup()
board.fd(50)
board.right(90)
board.forward(25)
board.left(135)
board.pendown()

for i in range(4):
    board.fd(100)
    board.left(90)

turtle.done()