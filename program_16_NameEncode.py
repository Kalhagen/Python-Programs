#----------------------------------------------------------
# These websites are a good reference for Tk
# http://www.tkdocs.com/tutorial/index.html
# http://www.pythonware.com/library/tkinter/introduction/
#----------------------------------------------------------

#---------------------------------------------------------------
# This program uses Python tkinter to create a text encoder.
# The user types in a string of characters in a text box,
# the program then encodes each character according to an
# encoder (dictionary) and prints the result on the window.
#
# There are two encoders, a Reverse encoder, that simply 
# reverses the order of the string.printable characters,
# and a Numeric encoder, that uses the index value of the
# characters found in string.printable
#---------------------------------------------------------------

#---------------------------------------------------------------
# The ttk module is the 'tk themed widgets'
# It overrides and improves some of the basic tkinter widgets.
# ttk comes with 17 widgets, 11 of which already existed in tkinter: 
# Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, 
# PanedWindow, Radiobutton, Scale and Scrollbar. 
# The other six are new: Combobox, Notebook, Progressbar, Separator, 
# Sizegrip and Treeview.
from tkinter import *
from tkinter import ttk

import string

#---------------------------------------------------------------
class MessageEncoder:

    # Note that a tkinter Tk() StringVar() can not be created
    # until after the root widget is created: root = Tk()
    # The StringVar() has get() and set() methods that allow you
    # to get and set values from the widgets. Note that we set
    # the initial value of encoderType to StringVar(value = 'Reverse')
    def __init__(self):
        self.inputText      = StringVar() # defined in tkinter Tk()
        self.encodedName    = StringVar()
        self.encoderType    = StringVar(value = 'Reverse') # or 'Numeric'
        self.encoder        = None # reverseEncoder or numericEncoder
        self.reverseEncoder = {}   # dictionary for reverseEncoder
        self.numericEncoder = {}   # dictionary for numericEncoder


    def CreateEncoders(self):
        # here is where we create the encoders : setup whatever you like
        # the basic idea is to have a dictionary that maps each
        # letter typed in by the user to a value in the dictionary
        # (encoder)

        # create a tuple of the printable letters to use
        # as the dictionary keys, have to use a tuple since they
        # are immutable, and dicionary keys must be immutable
        keys = tuple( string.printable )

        # create a reversed version of the printable letters
        # first you have to create the list, then reverse it
        # we have to use a list, since lists are sequences that
        # can be changed (not immutable)
        revkeys = list( string.printable )
        revkeys.reverse()

        # now fill in the reverseEncoder dictionary
        for i in range( len( keys ) ) :
            self.reverseEncoder[ keys[i] ] = revkeys[ i ]

        # make the numeric encoder
        # this will map each letter to it's sequence number
        for i in range( len( keys ) ) :
            self.numericEncoder[ keys[i] ] = i

        #print('CreateEncoder',keys)
        #print('CreateEncoder',self.numericEncoder.keys())
        

    def SetEncoder(self):
        # The get() function gets the value from the widget
        # and copies it into the variable. This get() function
        # is part of the StringVar() type
        if self.encoderType.get() == 'Reverse' :
            self.encoder = self.reverseEncoder
            
        elif self.encoderType.get() == 'Numeric' :
            self.encoder = self.numericEncoder
            
        else:
            self.encoder = self.reverseEncoder

        # print('SetEncoder:', self.encoderType )
            

    def Encode(self, *args):
        # set the selected encoder
        self.SetEncoder() 

        # this is clunky since python strings are immutable
        # you can't change their value or append to them
        # First, get what the user typed in
        inputName = self.inputText.get()

        # create a list to hold the encoded letters
        # since we can't append to a string
        encodedNameList = []

        # for each letter in the inputName get the encoded value
        # from the encoder (dictionary) lookup. 
        # use str() to ensure that integers get processed as strings
        for i in range( len( inputName ) ) :
            encodedNameList.append( str( self.encoder[ inputName[i] ] ) )

        #print(encodedNameList)

        # join all the encoded letters into a string
        # since 'abc' is a string, '' is an empty string
        # so we use ''.join() to call the string join method
        # on the encodedNameList and put the result into encodedName
        encodedName = ''.join( encodedNameList )

        # set the encodedName into the class object for Tk
        self.encodedName.set( encodedName )

#---------------------------------------------------------------
root = Tk()
root.title('Message Encoder')

encoder = MessageEncoder()
encoder.CreateEncoders()

# Create the main widget Frame (window)
mainframe = ttk.Frame( root, padding = "3 3 12 12" )

# Setup the window layout and resize control with the 'grid'
# geometry manager. The earlier programs used 'pack', but 
# grid gives you control by letting you define what columns
# and rows you want to place a widget in.
# This is the main window, so we set it to use column = 0, row = 0
# The value of the "sticky" option is a string of 0 or more of the 
# compass directions N S E W, specifying which edges of the cell the 
# widget should be "stuck" to.
mainframe.grid( column = 0, row = 0, sticky=(N, W, E, S) )

# Every column and row has a "weight" grid option associated with it, 
# which tells it how much it should grow if there is extra room in 
# the master to fill. By default, the weight of each column or row 
# is 0, meaning don't expand to fill space. Here we set the weight
# to 1 telling the widget to expand and fill space as the window 
# is resized. 
mainframe.columnconfigure( 0, weight = 1 )
mainframe.rowconfigure   ( 0, weight = 1 )

# Create a text entry box for the input message
msgEntry = ttk.Entry( mainframe, width = 30, textvariable = encoder.inputText )

# Create a Label on the window to hold the encoded message
msgOutput = ttk.Label( mainframe, textvariable = encoder.encodedName )

# Create a button to press to run the encoder
# Tell the button to call encoder.Encode() when it is pressed
encodeButton = ttk.Button( mainframe, text="Encode",
                           command = encoder.Encode )

# Create some labels to hold text that explains what is what
text1 = ttk.Label(mainframe, text = "This text:")

text2 = ttk.Label(mainframe, text = "encodes to:")

# Create two radio buttons to select the encoder
# This one will set encoder.encoderType to 'Reverse' and 
# call the encoder.SetEncoder() method when selected
encoderSelectReverseRB = ttk.Radiobutton(mainframe, text = "Reverse",
                                         command  = encoder.SetEncoder,
                                         variable = encoder.encoderType,
                                         value = 'Reverse')

# This one will set encoder.encoderType to 'Numeric' and 
# call the encoder.SetEncoder() method when selected
encoderSelectNumericRB = ttk.Radiobutton(mainframe, text = "Numeric",
                                         command  = encoder.SetEncoder,
                                         variable = encoder.encoderType,
                                         value = 'Numeric')

# Setup the grid to control the format/placement of the widgets
# This application has 3 columns and 3 rows
# The columns & rows are numbered from 0 to 2
# -----------------------------------------
#  col 0 row 0 | col 1 row 0 | col 2 row 0 |
# -----------------------------------------|
#  col 0 row 1 | col 1 row 1 | col 2 row 1 |
# -----------------------------------------|
#  col 0 row 2 | col 1 row 2 | col 2 row 2 |
# -----------------------------------------
msgEntry.grid              ( column = 1, row = 0, sticky = (W, E) )
msgOutput.grid             ( column = 1, row = 1, sticky = (W, E) )
encodeButton.grid          ( column = 2, row = 2, sticky = W )
text1.grid                 ( column = 0, row = 0, sticky = W )
text2.grid                 ( column = 0, row = 1, sticky = W )
encoderSelectReverseRB.grid( column = 0, row = 2, sticky = W )
encoderSelectNumericRB.grid( column = 1, row = 2, sticky = W )

# for each widget in the mainframe, set some padding around
# the widget to space things out and look better
for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

# Set the focus on the msgEntry text box so that when the
# program starts anything typed will be set into the msgEntry box
msgEntry.focus()

# Bind the Enter key to the encoder.Encode() method
# This way, pressing Enter on the keyboard will do the same
# thing as pressing the encodeButton: call encoder.Encode()
root.bind('<Return>', encoder.Encode)

# Enter the Tk mainloop to service the window
root.mainloop()
