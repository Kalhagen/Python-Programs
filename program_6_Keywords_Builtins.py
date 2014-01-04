
# keywords define the Python language
keywordList = [
'False',      'class',      'finally',    'is',         'return',
'None',       'continue',   'for',        'lambda',     'try',
'True',       'def',        'from',       'nonlocal',   'while',
'and',        'del',        'global',     'not',        'with',
'as',         'elif',       'if',         'or',         'yield',
'assert',     'else',       'import',     'pass',
'break',      'except',     'in',         'raise' ]

# built-ins are functions that are always available
# other functions can be imported from modules, like math
builtinFunctionString = '''abs() dir() hex() next() slice() 
all() divmod() id() object() sorted() 
any() enumerate() input() oct() staticmethod() 
ascii() eval() int() open() str() 
bin() exec() isinstance() ord() sum() 
bool() filter() issubclass() pow() super() 
bytearray() float() iter() print() tuple() 
bytes() format() len() property() type() 
chr() frozenset() list() range() vars() 
classmethod() getattr() locals() repr() zip() 
compile() globals() map() reversed() __import__() 
complex() hasattr() max() round()   
delattr() hash() memoryview() set()   
dict() help() min() setattr()'''


# Use the main() function to print the list and string
def main():
    print("These are Python keywords, you can't use them for "
          "variable or function names: ")
    
    for keyword in keywordList :
        print( keyword, ' ', end='')
    print()
    print()

    print("These are 'built-in' functions:")
    print(builtinFunctionString)
    
# This tells Python to run the function called main()
if __name__ == "__main__":
    main()
