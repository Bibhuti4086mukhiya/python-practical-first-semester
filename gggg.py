import turtle
turtle.Turtle()
for i in range(50):
  turtle.circle(10*i)
  turtle.up()
  turtle.sety((10*i)*(-1))
  turtle.down()