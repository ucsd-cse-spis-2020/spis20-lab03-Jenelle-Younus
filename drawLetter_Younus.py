"""This program will draw my first Initial "Y"""


import turtle
#Function to draw the first letter in my name
def drawY(theTurtle):
  #First line in Y
  theTurtle.left(45)
  theTurtle.forward(100)
  #Reset position
  theTurtle.penup()
  theTurtle.setpos(0,0)
  theTurtle.pendown()
  #Draws the second line
  theTurtle.left(90)
  theTurtle.forward(100)
  #Resets position
  theTurtle.penup()
  theTurtle.setpos(0,0)
  #Draws the vertical line
  theTurtle.pendown()
  theTurtle.left(135)
  theTurtle.forward(100)
  
theTurtle = turtle.Turtle()   #Creates turtle to draw letter Y
verifyTurtle = turtle.Turtle() #Creates a second test turtle
theTurtle.pencolor(240, 160, 80)  #Sets pencolor to gold
drawY(theTurtle)
drawY(verifyTurtle) #Calls drawY with a second turtle to verify it works
