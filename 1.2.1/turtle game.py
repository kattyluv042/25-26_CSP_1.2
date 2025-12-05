#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
#Score turtle
score_writer = trtl.Turtle()
score_writer.penup()

# Turtle to draw box
box_turtle = trtl.Turtle()
box_turtle.penup()

#
umbreon = trtl.Turtle()
umbreon.shape("circle")
umbreon.color(spot_color)
umbreon.shapesize(3)
umbreon.penup()

#-----game functions--------
# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    #Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    # Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 335)

    # Hide the turtles
    score_writer.hideturtle()
    box_turtle.hideturtle()


def spot_clicked(x, y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    umbreon.goto(newX, newY)
    update_score()

def update_score():
    # includes the global score
    global score
    # increments the score by 1
    score += 1
    # Clear out prior score
    score_writer.clear()
    # prints the score
    score_writer.write(score, font=font_setup)


#-----events----------------
umbreon.onclick(spot_clicked)

scoreBox()
wn = trtl.Screen()
wn.mainloop()