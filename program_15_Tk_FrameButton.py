#----------------------------------------------------------
# These websites are a good reference for Tk
# http://www.tkdocs.com/tutorial/index.html
# http://www.pythonware.com/library/tkinter/introduction/
#----------------------------------------------------------

import tkinter as tk

##-------------------------------------------------------------------
## This sample application is written as a class.
## The constructor (the __init__ method) is called with a
## parent widget (the rootWidget), to which it adds a number of
## child widgets. The constructor starts by creating a Frame
## widget. A frame is a simple container, and is in this case is
## only used to hold the other two button widgets.
##-------------------------------------------------------------------
class App:
    def __init__(self, rootWidget):
        # The frame instance is stored in a local variable called frame.
        # After creating the widget, we call the pack method geometry
        # manager to control the frame placement.
        frame = tk.Frame(rootWidget)
        frame.pack()

        # Create two Button widgets, as children to the frame.
        # This button calls the function frame.quit() when it is
        # pressed to end the program
        self.button = tk.Button(frame, text = "QUIT", fg = "red",
                                command = frame.quit)
        # call pack from the button to control it's placement
        self.button.pack(side = tk.LEFT)

        # This button calls the App.say_hi() function when the
        # button is pressed
        self.hi_there = tk.Button(frame, text = "Hello",
                                  command = self.say_hi)
        self.hi_there.pack(side = tk.LEFT)

    # The "hello" button callback is given next. It simply prints
    # a message to the console everytime the button is pressed:
    def say_hi(self):
        print("Hi there, everyone!")

#-------------------------------------------------------------------
# Create the Tk root widget
root = tk.Tk()

# Create one instance of the App class using the
# root widget as its parent:
app = App(root)

# Call the Tk event loop
root.mainloop()

# This call onl works if the Quit button is pressed.
# If the user selects the main window quit, it will error. 
root.destroy()
