import math

def Strings():
    # strings hold letters and characters
    string1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string2 = "0123456789"
    string3 = "A double quote string can hold 'single' quotes."
    string4 = """'Triple quoted' strings are used for long
 strings that may be more than one line long."""
    string5 = '''Triple quoted holds anything: ' " \ % '''

    stringList = [ string1, string2, string3,
                   string4, string5 ]

    for eachString in stringList :
        print( eachString )

    print("You can add (concatenate) strings:")
    print( string1 + string2 )
    print( string1, string2, string1[0:10], sep = ' : ' )

def Numbers():
    # Numbers are called floats (floating point) or int (integer)
    float1 = math.pi
    float2 = 1.5544332211
    int1   = 25
    int2   = 12

    print('float1 = ', float1, '  int1 = ', int1 )

    # add the numbers together into a variable called numberSum
    numberSum = float1 + float2 + int1 + int2 
    print('The sum is:', numberSum)

    print('Using the sum() function:', sum( [float1, float2, int1, int2] ) )

# Use the main() function to call the other functions
def main():
    Strings()
    Numbers()
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
