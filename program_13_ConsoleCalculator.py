
#-----------------------------------------------------------------
# 
class ConsoleCalculator:
    def __init__(self):
        self.Continue  = True
        self.inputLine = None
        self.operation = None
        self.number1   = 0.
        self.number2   = 0.
        self.answer    = 0.

        print('Welcome to the ConsoleCalculator')
        print('   to exit type in q')
        print('   enter equations with spaces: 2 + 2')

    def ReadInput(self):
        self.inputLine = input('Input > ')
        
        if 'q' in self.inputLine:
            self.Continue = False
            return

        # assume there a 3 input tokens: 3.4 + 4.2
        # break the inputLine into separate 'words'
        words = self.inputLine.split()

        # make sure there are a least 3 words
        if  len(words) < 3:
            print('Error > Not enough input')
            self.number1   = 0.
            self.number2   = 0.
            self.operation = None
        else:
            self.number1   = float( words[0] )
            self.operation = words[1]
            self.number2   = float( words[2] )
        
    def ComputeAnswer(self):

        if self.operation == '+':
            self.answer = self.number1 + self.number2
        elif self.operation == '-':
            self.answer = self.number1 - self.number2
        elif self.operation == '*':
            self.answer = self.number1 * self.number2
        elif self.operation == '/':
            self.answer = self.number1 / self.number2
        else :
            print('Error > Failed to understand the operation')
            self.answer = 0.            
    
        print('Answer> ', self.answer )

#-----------------------------------------------------------------
def main():

    # create (instantiate) the ConsoleCalculator
    calc = ConsoleCalculator()

    while True:
        calc.ReadInput()
        if not calc.Continue :
            break

        calc.ComputeAnswer()
    
# Tell Python to run the main() function
if __name__ == "__main__":
    main()
