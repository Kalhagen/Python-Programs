
# modules allow us to 'import' functions that other
# people wrote

import program_9_dictionary as pop
import math
import random

def main():
    pop.PrintStatePopInfo()
    pop.FindStatePopulation()

    print()
    print('The value of pi is', math.pi )
    print('The square root of pi is', math.sqrt( math.pi ) )

    print()
    print('Here are 10 random numbers between 1 and 100:')
    for i in range(0,10) :
        print( random.randint(1, 100), ' ', end='' )
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
