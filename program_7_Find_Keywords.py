
# keywords define the Python language
keywordList = [
'False',      'class',      'finally',    'is',         'return',
'None',       'continue',   'for',        'lambda',     'try',
'True',       'def',        'from',       'nonlocal',   'while',
'and',        'del',        'global',     'not',        'with',
'as',         'elif',       'if',         'or',         'yield',
'assert',     'else',       'import',     'pass',
'break',      'except',     'in',         'raise' ]

# Scan a text file for Python keywords
def main():
    fileName = input('Enter the name of a python file: ')

    # open the file
    pyFile = open( fileName )

    # get a list of strings that hold the file contents
    # we call the pyFile object function 'readlines()'
    pyFileLineList = pyFile.readlines()

    # print some info about the file
    print("The file", fileName, "has", len(pyFileLineList), "lines.")

    # print the first 3 lines
    print("The first three lines are:")
    for line in pyFileLineList[0:3] :
        print(line)

    # lets see if we can find any keywords in the file
    for line in pyFileLineList :
        for keyword in keywordList:
            if line.find( keyword + ' ' ) > -1 :
                print("Found keyword:", keyword)
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
