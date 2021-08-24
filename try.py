import turtle
turtle.bgcolor('yellow')
def drawshape(turtle,radius):
    turtle.circle(radius,extent=60)
    turtle.left(99)
    turtle.circle(radius,extent=60 )
def drawflower():
    petal=turtle.Turtle()
    petal.color('black')
    petal.speed(0)
    petal.pensize(8)
    no_of_petals=8
    radius=200
    for i in range(no_of_petals):
        drawshape(petal,radius)
        petal.left(305 / no_of_petals)
drawflower()
turtle.done()
