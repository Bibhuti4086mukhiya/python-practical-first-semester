import turtle
p=turtle.Turtle()
w=turtle.Screen()
counter=10
while counter<=200:

    p.right(90)
    p.forward(counter)
    p.right(-90)
    
    p.circle(counter)

    p.home()
    counter=counter+50
turtle.done()
