#when the comman python3 ex.py is run , ex.py is the argument. 
#Now, this specific python script will take an argument. 

#This first line calls the module argv which stands for argument variable.
from sys import argv

#The argument variable stores arguments that will be passed when the program is run.
script, first, second, third = argv

print('The script is called:', script)
print('The first variable is:', first)
print('The second variable is:', second)
print('The third variable is:', third)