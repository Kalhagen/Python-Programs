# This is a comment since it starts with #
# Comments are notes for the programmer
# The computer ignores comments.

# The main function definition
def main():
    # Ask the user to type in their name
    # Save the answer in the variable myName
    myName = input('Type in your name: ')

    # Tell the user how many letters are in their name
    print( 'Your name is', myName )
    print( myName, 'is', len(myName), 'letters long.')

    # Make a list of known boy and girl names
    girlNames = ['Kate', 'Sabrina', 'Kelly', 'Marsha', 'Jill']
    boyNames  = ['Chad', 'Roger', 'William', 'Charles', 'Joseph']

    # Based on the user's name, and the list of names we have
    # try to decide if the the name is male or female
    if ( myName in girlNames ):
        print( myName, 'is a girls name.' )
    elif ( myName in boyNames ):
        print( myName, 'is a boys name.' )
    else:
        print( "Can't tell if", myName, "is a boy or girl name." )
        print( "These are all the girl names:", girlNames )
        print( "And these are all the boy names:", boyNames )

# This tells Python to run the function called main()
# Programs usually have many of functions, so this makes
# the one called main() the starting function for this program.
# When you start putting your program functions in modules, 
# this also provides a way to ignore this main function.
if __name__ == "__main__":
    main()
