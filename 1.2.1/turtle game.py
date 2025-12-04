#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
def spot_clicked(x, y):
    # Move the turtle to a random location
    print("turtle was clicked")
    meowl.pendown()
    meowl.goto(x, y)


#-----events----------------
meowl.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()