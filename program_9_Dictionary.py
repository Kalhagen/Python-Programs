
# Dictionaries are paired lists 
# a 'key' is used to access a value { key : value }
# Note that a dictionary is defined with '{}' a list with '[]'
statePopulation = {'Alabama'    : 4779736,
                   'Alaska'     : 710230,
                   'Arizona'    : 6392017,
                   'Arkansas'   : 2915918,
                   'California' : 37253956,
                   'Colorado'   : 5029196,
                   'Conneticut' : 3574097,
                   'Delaware'   : 879934,
                   'Florida'    : 18801310,
                   'Georgia'    : 9687653,
                   'Hawaii'     : 1360301,
                   'Idaho'      : 1567582,
                   'Illinois'   : 12830632,
                   'Indiana'    : 6483802,
                   'Iowa'       : 3046355,
                   'Kansas'     : 2853118 }

def PrintStatePopInfo():
    print('My database has', len(statePopulation), 'states in it.')
    
    totalPopulation = sum( statePopulation.values() )

    print('The total population is', '{:,}'.format(totalPopulation))


def FindStatePopulation():
    FindPopulation = input('Do you want to find a state population? yes/no : ')
    
    if ( FindPopulation == 'yes' ) :
        stateName = input('Enter the state you want to check ')

        if stateName in statePopulation.keys() :
            print('The population of', stateName,
                  'is', statePopulation[stateName] )
        else:
            print('The state', stateName, "isn't in my database.")
        

def main():
    PrintStatePopInfo()
    FindStatePopulation()
    
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
