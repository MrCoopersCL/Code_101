#whenever an exception occurs it is written to std error 

import sys

def print_to_stderr(*a):
    #here is the array holding the objects
    #passed as the argument of the function 
    print(*a, file = sys.stderr)

print_to_stderr("Hello World")

#You can use this to warn the user
integer_input = 4.6

if type(integer_input) == int:
    print('You win!')
elif type(integer_input) == float:
    print_to_stderr("ERROR: PLEASE ENTER INTGER")
elif type(integer_input) == str:
    print_to_stderr("ERROR: PLEASE ENTER INTGER")
    
#remember this will not halt the program!
elif type(integer_input) == bool:
    print_to_stderr("ERROR: PLEASE ENTER INTGER")
