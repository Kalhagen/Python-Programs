#----------------------------------------------------------
# These websites are a good reference for Tk
# http://www.tkdocs.com/tutorial/index.html
# http://www.pythonware.com/library/tkinter/introduction/
#----------------------------------------------------------

#---------------------------------------------------------------------
# This program shows how to use a Tk Canvas to draw using the mouse
#---------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

# These global variables hold the coordinates ( x, y ) of the mouse
xCoord = 0
yCoord = 0

# These global variables are the pen color and width
color     = "black"
lineWidth = 1.

#---------------------------------------------------------------------
# function setXY is called when the mouse button 1 is pressed.
# It stores the x, y values of the mouse into the global variables.
# Note that we have to declare the xCoord, yCoord as global
# otherwise we can't write new values to them from inside
# a function
#---------------------------------------------------------------------
def setXY(event):
    global xCoord, yCoord

    xCoord = event.x
    yCoord = event.y

#---------------------------------------------------------------------
# function setColor() changes the color of the pen
# the newColor is passed in, and then used to set the global color
#---------------------------------------------------------------------
def setColor(newColor):
    global color
    color = newColor

#---------------------------------------------------------------------
# function setLineWidth() changes the color of the pen
# the newColor is passed in, and then used to set the global color
#---------------------------------------------------------------------
def setLineWidth(newWidth):
    global lineWidth
    lineWidth = newWidth

#---------------------------------------------------------------------
# function addLine() draws a line as the mouse is moved with
# the first button held down
#---------------------------------------------------------------------
def addLine(event):
    global xCoord, yCoord

    # use the Canvas().create_line() method
    # Note that the line is drawn from the xCoord, yCoord which
    # is the starting point (the last values of x, y) and is 
    # drawn to event.x, event.y which come from the mouse
    canvas.create_line((xCoord, yCoord, event.x, event.y), 
                       fill = color, width = lineWidth)

    # update the x, y coordinates to the ending position
    setXY(event)

#---------------------------------------------------------------------
# delete all items from the canvas and redraw the legend
#---------------------------------------------------------------------
def Clear(event):
    # Note that the canvas is created in the main section below
    canvas.delete(ALL)
    CreateLegend()

#---------------------------------------------------------------------
# Create 3 color rectangles that the user can click on to
# change the color of the pen, and 3 lines the user can 
# click to set the line width
#---------------------------------------------------------------------
def CreateLegend():
    # this creates a red rectangle
    id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
    # this binds the setColor("red") function to the mouse click
    canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
    
    id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
    canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
    
    id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
    canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))	

    # this creates a thin vertical line
    id = canvas.create_line((10, 90, 10, 120), 
                            fill = "black", width = 1.0)
    # this binds the setLineWidth(1.0) function to the mouse click
    canvas.tag_bind(id, "<Button-1>", lambda x: setLineWidth(1.0))	
    
    id = canvas.create_line((20, 90, 20, 120), 
                            fill = "black", width = 3.0)
    canvas.tag_bind(id, "<Button-1>", lambda x: setLineWidth(3.0))	

    id = canvas.create_line((30, 90, 30, 120), 
                            fill = "black", width = 6.0)
    canvas.tag_bind(id, "<Button-1>", lambda x: setLineWidth(6.0))	

#---------------------------------------------------------------------
root = Tk()
root.title('Tk Canvas Draw')

# Tell the root window to resize to fill all available space
root.columnconfigure(0, weight = 1)
root.rowconfigure   (0, weight = 1)

# Create the Tk Canvas to draw on 
canvas = Canvas(root)
canvas.grid( column = 0, row = 0, sticky=(N, W, E, S) )

# Connect the mouse button to the functions setXY, addLine and Clear
canvas.bind("<Button-1>",  setXY)    # Button-1 is the left button
canvas.bind("<B1-Motion>", addLine)  # Button-1 press plus moving mouse
canvas.bind("<Button-3>",  Clear)    # Button-3 is the right button

CreateLegend()

root.mainloop()
