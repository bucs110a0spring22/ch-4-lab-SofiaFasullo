import math
import turtle

wn = turtle.Screen()
fred = turtle.Turtle()

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(myturtle=None):
  for i in range(-360,360):
    i=i+1
    myturtle.goto(i,math.sin(math.radians(i)))
#drawSineCurve(fred)

def setupWindow(mywindow=None):
  mywindow.setworldcoordinates(-360,-1,360,1)
  mywindow.bgcolor('beige')

def setupAxis(myturtle=None):
  myturtle.clear()
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()
  myturtle.goto(360,0)
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.goto(0,1)
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
