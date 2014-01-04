#----------------------------------------------------------
# These websites are a good reference for Tk
# http://www.tkdocs.com/tutorial/index.html
# http://www.pythonware.com/library/tkinter/introduction/
#----------------------------------------------------------

from tkinter import *
from tkinter import ttk

#----------------------------------------------------------------
# This program will use the database (dictionary) of US States
# from program_12_States.py to allow the user to select multiple
# states from a Tk Listbox. When states are selected, their
# database information is displayed in a Label widget. It also
# allows the user to select from a checkbutton which information
# they would like to display. 
#----------------------------------------------------------------

# Create a UnitedStates object from program_12_States
import program_12_States
US = program_12_States.UnitedStates()

# Fill in the database from the file with the US.ReadDataFile() method
US.ReadDataFile( 'US_States.csv' )

# Get a list of the state names from the US_database
# We will show this list in the Listbox
stateNames = list( US.US_database.keys() )

# Since this list is from dictionary keys, the order is random
# sort them alphabetically
stateNames.sort()

# Initialize Tk, must be prior to creation of StringVar()
root = Tk()
root.title('US States Database')

# Tk I/O variables
# valid types are BooleanVar, DoubleVar, IntVar, StringVar
# This holds the outputMessage with all the information
outputMessage = StringVar()
# These are I/O variables for the checkbuttons
dateFounded_CB_value = BooleanVar( value = True  )
USPS_CB_value        = BooleanVar( value = False )
capital_CB_value     = BooleanVar( value = False )
population_CB_value  = BooleanVar( value = False )
area_CB_value        = BooleanVar( value = False )
biggestCity_CB_value = BooleanVar( value = False )

#----------------------------------------------------------------
# When the user selects an item from the Listbox, this callback
# function process the selected state by extracting the stored
# information from the US_database and updating the message 
# text in outputMessage. The outputMessage is then displayed
# in the Label widget. 
#----------------------------------------------------------------
def ProcessListbox(*args):
    # Get the indexes of the state selected in the ListBox
    i_selected = lbox.curselection() # a tuple of indices as text

    # convert the tuple of text indicies into a list of integers
    i_selected_int = []

    for i in i_selected :
        i_selected_int.append( int( i ) )

    msg = '' # initialize an empty string to hold the output

    for i in i_selected_int :
        # we assume that the i corresponds to the index in stateNames 
        dateFounded = US.US_database[ stateNames[i] ].dateFounded
        USPS        = US.US_database[ stateNames[i] ].USPS
        capital     = US.US_database[ stateNames[i] ].capital
        population  = US.US_database[ stateNames[i] ].population
        area        = US.US_database[ stateNames[i] ].area
        biggestCity = US.US_database[ stateNames[i] ].biggestCity

        # Create an output message from the data
        msg = msg + stateNames[i]

        if dateFounded_CB_value.get() :
            msg = msg + ' was founded ' + dateFounded + '\n'

        if capital_CB_value.get() :
            msg = msg + 'The capital is ' + capital + '\n'

        if biggestCity_CB_value.get() :
            msg = msg + 'The largest city is ' + biggestCity

        if population_CB_value.get() :
            msg = msg + 'The population is ' + population + '\n'

        if area_CB_value.get() :
            msg = msg + 'The area is ' + area  + '\n\n'

    outputMessage.set(msg)

#----------------------------------------------------------------
# Create and grid the outer content frame
mainFrame = ttk.Frame( root, padding=(5, 5, 12, 0) )
mainFrame.grid( column = 0, row = 0, sticky = (N,W,E,S) )

# These grid_*configure functions make the widgets in the
# rows and columns expand as the root window is resized
# if weight = 0, there is no resize, if weight = 1, then
# resize to fill the whole window
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure   (0, weight=1)

# Create the Listbox to hold the state names
lbox = Listbox( mainFrame, height = 10, selectmode = EXTENDED )

# Insert the state names into the Listbox
# The listvariable = [] option won't work if
# there is whitespace in a name, so insert them manually
for i in range( len(stateNames) ) :
    lbox.insert( i, stateNames[i] )

# Create a Label to hold the outputMessage
stateInfo = ttk.Label( mainFrame, textvariable = outputMessage, anchor = E )

# Create a vertical scroll bar for the Listbox
# Tell the scrollbar that it will call the Listbox yview function
# when the user moves the scrollbar
scrollBar = ttk.Scrollbar( mainFrame, orient = VERTICAL, command = lbox.yview )

# Tell the Listbox that it will scroll according to the scrollBar
lbox.configure( yscrollcommand = scrollBar.set )

# Create a series of checkbuttons to allow the user to 
# specify which database items they want to display
dateFounded_CB = ttk.Checkbutton(mainFrame, text = 'Date Founded', 
                                 command  = None, 
                                 variable = dateFounded_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

USPS_CB        = ttk.Checkbutton(mainFrame, text = 'Postal Code', 
                                 command  = None, 
                                 variable = USPS_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

capital_CB     = ttk.Checkbutton(mainFrame, text = 'Capital', 
                                 command  = None, 
                                 variable = capital_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

population_CB  = ttk.Checkbutton(mainFrame, text = 'Population', 
                                 command  = None, 
                                 variable = population_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

area_CB        = ttk.Checkbutton(mainFrame, text = 'Area', 
                                 command  = None, 
                                 variable = area_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

biggestCity_CB = ttk.Checkbutton(mainFrame, text = 'Major City', 
                                 command  = None, 
                                 variable = biggestCity_CB_value,
                                 onvalue  = True, 
                                 offvalue = False)

#--------------------------------------------------------------
# Grid all the widgets - This is the layout of the window
# This application has 3 columns and 6 rows
# The Listbox and scrollbar are in column 0, 
# The outputMessage Label is in column 1
# Both the Listbox and outputMessage Label span multiple rows
# The checkbuttons are in column 2 and rows 0 - 5
# padx = 23 prevents overlap with the scrollbar
lbox.grid( column = 0, row = 0, rowspan = 6, padx = 23, sticky=(N,S) )

scrollBar.grid( column = 0, row = 0, rowspan = 6, sticky = (W,N,S) )

stateInfo.grid( column = 1, row = 0, rowspan = 6, sticky=(N,S,W,E) )

dateFounded_CB.grid( column = 3, row = 0, sticky = W )
USPS_CB       .grid( column = 3, row = 1, sticky = W )
capital_CB    .grid( column = 3, row = 2, sticky = W )
population_CB .grid( column = 3, row = 3, sticky = W )
area_CB       .grid( column = 3, row = 4, sticky = W )
biggestCity_CB.grid( column = 3, row = 5, sticky = W )

# Don't resize the column 0 - the width of the Listbox
mainFrame.grid_columnconfigure(0, weight = 0)

# Resize the column 1 & 2 and rows as the window is resized
mainFrame.grid_columnconfigure(1, weight = 1)
mainFrame.grid_columnconfigure(2, weight = 1)
mainFrame.grid_rowconfigure   (0, weight = 1)
mainFrame.grid_rowconfigure   (1, weight = 1)
mainFrame.grid_rowconfigure   (2, weight = 1)
mainFrame.grid_rowconfigure   (3, weight = 1)
mainFrame.grid_rowconfigure   (4, weight = 1)
mainFrame.grid_rowconfigure   (5, weight = 1)

# This tells the Listbox to call the functin ProcessListbox()
# when the selection in the listbox changes
lbox.bind('<<ListboxSelect>>', ProcessListbox)

# Colorize alternating lines of the listbox
for i in range( 0, len(stateNames), 2):
    lbox.itemconfigure( i, background = '#f0f0ff' )

# Set the starting state of the interface by selecting
# the first state in the list and calling ProcessListbox()
lbox.selection_set(0)
ProcessListbox()

# Enter the main event loop 
root.mainloop()
