#----------------------------------------------------------
# These websites are a good reference for Tk
# http://www.tkdocs.com/tutorial/index.html
# http://www.pythonware.com/library/tkinter/introduction/
#----------------------------------------------------------

#----------------------------------------------------------
# This program is a simple GUI (Graphical User Interface)
# using the tkinter module from Python
#----------------------------------------------------------

# import the tkinter module and label it as 'tk'
import tkinter as tk

# To initialize tkinter, we have to create a Tk root widget.
# This is the main window, with a title bar and other
# decoration provided by your window manager. You should only
# create one root widget for each program, and it must be
# created before any other widgets.
root = tk.Tk()

# Create a Label widget as a child to the root window.
# A Label widget can display either text or an icon or other image. 
# We use the text option to specify which text to display. 
labelWidget = tk.Label( root, text = "Hello, world!" )

# Next, we call the pack method on this widget. 
# pack() is a 'geometry manager' which controls the placement
# and size of the widgets. It also controls how the widget 
# resizes itself to hold the text, or when the main window is resized.
labelWidget.pack()

# The tkinter event loop runs the program
root.mainloop()
