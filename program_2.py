def main():
    myName = input('Type in your name: ')

    print( 'Your name is', myName )
    print( myName, 'is', len(myName), 'letters long.')

    girlNames = ['Kate', 'Sabrina', 'Kelly', 'Marsha', 'Jill']
    boyNames  = ['Chad', 'Roger', 'William', 'Charles', 'Joseph']

    if ( myName in girlNames ):
        print( myName, 'is a girls name.')
    elif ( myName in boyNames ):
        print( myName, 'is a boys name.')
    else:
        print("Can't tell if", myName, "is a boy or girl name")

if __name__ == "__main__":
    main()
