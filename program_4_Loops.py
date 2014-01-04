def main():
    # Loops do things more than once
    # the loop keywords are: for and while

    # for loops work on sequences (lists, arrays, dictionaries...)
    # make a list of animals in a zoo
    zoo = ['Tiger', 'Bear', 'Snake', 'Lion', 'Dog', 'Cat']

    print("\nMy zoo has", len(zoo), 'animals.')

    print("The animals in my zoo are:")
    for animal in zoo :
        print( animal )

    # Sequences can always be accessed by an index
    print("\nAnother way to see the animals in the zoo:")
    for i in range( len(zoo) ) :
        print( 'animal', i, 'is a', zoo[i] )


    # break tells a loop to 'break out'
    print("\nSome of the animals in my zoo are:")
    for animal in zoo :
        if animal == zoo[3] :
            break
        
        print( animal )
    

if __name__ == "__main__":
    main()
