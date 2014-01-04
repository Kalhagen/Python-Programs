
# Create a list of state names
stateList1 = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']

stateList2 = ['Colorado', 'Conneticut', 'Delaware', 'Florida', 'Georgia']

stateList3 = ['Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas']

# a function to print the functions of a list
def PrintListFunctions():
    listFunctions = ['append', 'count', 'extend', 'index',
                     'insert', 'pop', 'remove', 'reverse', 'sort']

    print('The functions that belong to a list are:')
    for function in listFunctions :
        print( function, ' ', end='' )
        
    print()

def ShowListFunctions():
    # tell Python that we want to be able to change these
    # lists, even though they are not in this function
    global stateList1, stateList2, stateList3

    print('The first list is:', stateList1)

    # Add a state to the first list
    stateList1.append('Wyoming')
    # remove a state
    stateList1.remove('Alabama')
    print('The list was changed:', stateList1)

    print('The second list is:', stateList2)

    # reverse a list
    stateList2.reverse()
    print('This list was reversed:', stateList2)


def main():
    PrintListFunctions()
    ShowListFunctions()
    
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
