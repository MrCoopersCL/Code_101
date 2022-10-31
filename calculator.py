#Simple calculator. Takes two integers, performs an operation and creates an output.

print('Enter first number')
a = input('>>>')
print('''
-----------------------------------------------------------------------------------
Choose operation from following:
*MULTIPLY
*DIVIDE
*SUBTRACT
*ADD
-----------------------------------------------------------------------------------
''')
oper = input('>>>')

print('''
-----------------------------------------------------------------------------------
Enter Second number:
''')
b = input('>>>')
print('''
-----------------------------------------------------------------------------------
''')



if oper == 'MULTIPLY':
    print( int(a) * int(b)) 
elif oper == 'DIVIDE':
    print( int(a) / int(b))
elif oper == 'SUBTRACT': 
    print( int(a) - int(b)) 
elif oper == 'ADD':
    print( int(a) + int(b) ) 
else:
    print('Please Try Again')

     