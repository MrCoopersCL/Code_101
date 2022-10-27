#Topic: Functions 
#A function is a strategy decreasing repetition in code. 

#Convert the number 68 to binary code.
#A functions syntax starts with def 
def bin_fun():
    #^Then the function is named.
    #^open and closed parenthesis 
    #^The colon tells the function to start the functions code block (or body of the function). 
    
    #The contents of the functions code block will be what is executed when the function is called. 
    x = int(input('Please enter a number: '))
    
    #The return keyword is used here to exit the function and return its binary value. 
    return (bin(x))

#a function can be called in a print statement like a variable. 
print('Print your binary number is ', bin_fun())

#parameters are variables that are part of the function. 
#When the function is called, the parameter values are sent to the code in the functions body. 
#You can declare as many parameters as you want in a function.
#I recommend to only use as many parameters as you need. 
def bin_fun_2(a, b, c, d, e, f, g):
    bin_1 = bin(a)
    bin_2 = bin(b)
    bin_3 = bin(c)
    bin_4 = bin(d)
    bin_5 = bin(e)
    bin_6 = bin(f)
    bin_7 = bin(g)
    print('Your integer values are: ', a, b, c, d, e, f, g)
    print('Your binary values are : ', bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7)

#now when a function is called, values need to be supplied to the parameters. 
bin_fun_2(1, 2, 3, 4, 5, 6, 7)
bin_fun_2(10, 20, 30, 40, 50, 60, 70)
bin_fun_2(100, 200, 300, 400, 500, 600, 700)
bin_fun_2(1000, 2000, 3000, 4000, 5000, 6000, 7000)

#Instead of assigning a variable everytime for a block of code, parameters can accept different values for the same code. 

#On the next line, write a function that returns the area of a square. 




#Call the function. 



#Why don't snakes drink coffee? 
#~it makes them viperactive
