# Import turtle
import turtle as trtl

# Make a turtle
harper = trtl.Turtle()

def drawsquare(length):
    for sides in range(4):
        harper.forward(length)
        harper.right(90)

# Goal: to draw squares with a turtle

drawsquare(62)
harper.forward(100)
drawsquare(42)





wn = trtl.Screen()
wn.mainloop()
