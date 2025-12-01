# Import turtle
import turtle as trtl

# Make a turtle
harper = trtl.Turtle()

def drawsquare():
    for sides in range(4):
        harper.forward(30)
        harper.right(90)

# Goal: to draw squares with a turtle

drawsquare()


harper.forward(60)






wn = trtl.Screen()
wn.mainloop()