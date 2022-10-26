#Objective: Encode each character in a string to binary. Print the output. The String is 'BLUE'.
#First watch this video to see how ASCII is converted to binary by hand.
#We will try to replicate this using python code. 

#Define variables for each character to be encoded
character_B = 'B'
character_L = 'L'
character_U = 'U'
character_E = 'E'

#The bin method only works on integers. 
#ASCII stores a numeric value that the bin method can use.
ascii_value_B = ord(character_1)
ascii_value_L = ord(character_2)
ascii_value_U = ord(character_3)
ascii_value_E = ord(character_4)
#Note: ASCII values are integers between 0 and 127.

#With an ascii value assigned to each new variable the bin method can now be used. 
binary_B = bin(ascii_integer_B)
binary_L = bin(ascii_integer_L)
binary_U = bin(ascii_integer_U)
binary_E = bin(ascii_integer_E)

#Print the results to your terminal.  
print(f'Character: {character_B} | ASCII VALUE:{ascii_value_B} | BINARY CODE:{binary_B}')
print(f'Character: {character_L} | ASCII VALUE:{ascii_value_L} | BINARY CODE:{binary_L}')
print(f'Character: {character_U} | ASCII VALUE:{ascii_value_U} | BINARY CODE:{binary_U}')
print(f'Character: {character_E} | ASCII VALUE:{ascii_value_E} | BINARY CODE:{binary_E}')

#Now try it again with a string of your choice. Compare using a python script to convert a string to binary with converting by hand. Is it more or less difficult?
