
#-----------------------------------------------------------------
# define class StateInfo to hold information about each state
class StateInfo:
    def __init__(self):
        self.name        = None
        self.dateFounded = None
        self.USPS        = None
        self.capital     = None
        self.population  = None
        self.area        = None
        self.biggestCity = None

#-----------------------------------------------------------------
# define a class to hold and process the StateInfo
# for all the states
class UnitedStates:
    def __init__(self):
        # define a dictionary to hold the data
        # this will hold 50 instances of the StateInfo class
        self.US_database = {}

    def PrintStateInfo(self, state):
        print( self.US_database[ state ].name, end='' )
        print( ' was founded on ', self.US_database[ state ].dateFounded, end='' )
        print( ' the capital is ', self.US_database[ state ].capital )

    def ReadDataFile(self, fileName):
        dataFile = open(fileName)
        print('Opened file', fileName)

        # read all the file lines into a list of strings
        fileLines = dataFile.readlines()

        # Always close an open file when you are done reading
        dataFile.close()
        print('Closed file', fileName)

        # process each line and create a StateInfo for each one
        # skip the first line with the slice [1:]
        for line in fileLines[1:] :
            # create the new state class object
            newState = StateInfo()

            # break the line into 'words'
            # we know the line looks like this:
            # Name,USPS,Date,Area,Population,Capital,BiggestCity
            words = line.split(',')

            # we know the line has exactly 7 entries
            # if there are not 7 'words' found, raise an exception
            if len( words ) != 7 :
                errMsg = 'Failed to find 7 items in the line:\n' + \
                line + ' from the file: ' + fileName
                raise Exception(errMsg)

            # copy the 7 pieces of data that were read from the
            # file into the StateInfo class 
            newState.name        = words[0]
            newState.dateFounded = words[2]
            newState.USPS        = words[1]
            newState.capital     = words[5]
            newState.population  = words[4]
            newState.area        = words[3]
            newState.biggestCity = words[6]
           
            # insert the new state object into the US dictionary
            # the name of the state is the 'key' of the dictionary
            # and the StateInfo object is the 'value' for that key
            self.US_database[ newState.name ] = newState
            
        print('Added', len(self.US_database), 'states to the database.')
        

#-----------------------------------------------------------------
def main():
    # create the UnitedStates object
    US = UnitedStates()

    # use the US ReadDataFile() method
    US.ReadDataFile( 'US_States.csv' )

    # now that we have a database, we can ask some questions
    while True:
        askQuestion = input('Do you want to find a state? y/n ')
        if askQuestion != 'y' :
            break
        
        stateName = input('Enter a state name: ')
        
        if stateName not in US.US_database:
            print(stateName, ' is NOT in the database.')
            continue

        US.PrintStateInfo( stateName )
    
# Tell Python to run the main() function
if __name__ == "__main__":
    main()
