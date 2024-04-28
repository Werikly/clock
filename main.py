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

def drav_watchface(length, rotation):
   uzbek.penup()
   uzbek.home()
   uzbek.color("black")
   uzbek.forward(150)
   uzbek.pendown()
   uzbek.forward(length)

for i in range(0, 360, 30):
   uzbek.right(i)
   drav_watchface(20)

for i in range(0, 360, 6):
   uzbek.right(i)
   drav_watchface(10)


turtle.done