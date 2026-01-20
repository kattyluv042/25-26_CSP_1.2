import turtle as trtl


# Lists.
Colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]
SizeOfBrush =["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Direction writing setup
font_setup = ("Arial", 15, "normal")
directions = trtl.Turtle()
directions.penup()
directions.goto(-200, 0)
directions.write("Press the r,o,y,g,b,p,pk,bk to select a color from our color list", font=font_setup)
wn = trtl.Screen()
wn.mainloop()

# Key press setup