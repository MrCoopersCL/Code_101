#Now we will give our script more options using elif
pizza = 100
hotdogs = 50
turtles = 2

#elif allows the program to have more branches
if pizza == turtles:
    print('we have one slice for every turtle')
elif pizza > turtles:
    print('the turtles will feast!')
elif pizza < turtles:
    print('looks like the turtles will have to share.')
else:
    print("Hmmm...something isn't quite right")

#The first True condition of an if statement is the one that executes. 
if pizza > hotdogs:
    print('looks like its pizza for dinner')
elif hotdogs == hotdogs:
    print('the two variables are equivalent')
elif turtles == 2:
    print('there are two turtles')

#It is also useful to assign a variable an input value and then using that value as a test condition. 
dogs = input('Please enter number of dogs :')
cats = input('Please enter the number of cats :')

if dogs > cats:
    print(' So many dogs woof woof woof')
elif dogs < cats:
    print('Hide the tuna fish... the cats are here.')
else:
    print('I dont know what you mean.')
    
    
#Go ahead and read through this code as many times as needed so that it makes sense. 
#Next, declare different value ther variables above. What happens?
