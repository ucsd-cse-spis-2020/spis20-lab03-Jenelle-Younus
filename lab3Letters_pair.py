"""
Jenelle Truong and Younus Ahmad
1.The "anonymous turtle" is a turtle object that is implemented in python by default when a specific turtle is not instantiated or used to call the function.
2.Turtle() is a function call to create the object that references a specifically created turtle object, while turtle directs it to the turtle library built automatically into python.
3.myTurtle.sety(100)
"""

#This program will draw my first Initial "Y", of any inputed size


import turtle
#Function to draw the first letter in my name
def drawY(theTurtle, size):
  #First line in Y
  theTurtle.left(45)
  theTurtle.forward(size)
  #Reset position
  theTurtle.penup()
  theTurtle.setpos(0,0)
  theTurtle.pendown()
  #Draws the second line
  theTurtle.left(90)
  theTurtle.forward(size)
  #Resets position
  theTurtle.penup()
  theTurtle.setpos(0,0)
  #Draws the vertical line
  theTurtle.pendown()
  theTurtle.left(135)
  theTurtle.forward(size)
  
theTurtle = turtle.Turtle()   #Creates turtle to draw letter Y
theTurtle.pencolor(240, 160, 80)  #Sets pencolor to gold
size = 200
drawY(theTurtle, size)