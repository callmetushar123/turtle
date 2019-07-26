import turtle
x = 100
y=180
z=1
win = turtle.Screen()
ninja= turtle.Turtle()
#i=1;
#while(x!=0):
    #if(i%2!=0):
#alex.forward(150)
#alex.left(90)
#alex.forward(7)
#alex.left(90)
    #else:
    #    alex.forward(150)
    #    alex.right(90)
    #    alex.forward(1)


ninja.speed(50)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
