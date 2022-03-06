#
#  Example program for Targil 1
#
import math
from myboolfuncs import *
#

def sphereArea(r:float): 
    return 4*math.pi * r**2
def coneArea(r:float , h:float):
    return (1/3)*h*math.pi*r**2 
def squarePyramidArea(a:float,h:float):
    return 0.5 * a * h 
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
         radius = getNumber("Please enter the radius: ")
         area   = sphereArea(radius)
         print ("The area is", area)
         continue
    elif shape == "4":
         radius = getNumber("Please enter the radius: ")   
         width  = getNumber("Please enter the width: ")
         area   = coneArea(radius,width)
         print ("The area is", area)
         continue
    elif shape == "5":
         height = getNumber("Please enter the height: ")    
         areaBase = getNumber("Please enter the area of base: ")
         area   = squarePyramidArea(areaBase,height)
         print ("The area is", area)
         continue
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")