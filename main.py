import turtle


uzbek = turtle.Turtle()

turtle.setup(500, 500, 0, 0)
turtle.screensize(480, 480, bg="#ccc")
turtle.tracer(0)
turtle.hideturtle()

def draw_square(x, y, lenght):
    uzbek.penup()
    uzbek.home()
    uzbek.goto(x,y)
    uzbek.color("red")
    uzbek.pendown()

    for storona in range(4):
      uzbek.forward(lenght)
      uzbek.right(90)


turtle.done