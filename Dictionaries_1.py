#We can assign a value to a variable
manufacture = 'Ford'
model = 'mustang'
year = '2000'

print(manufacture, model, year)

#This is similiar to how dictionaries work.
#A dictionary assigns a value to a key.
dict = {'key':'value'}
print(dict)

#We can put data inside a dictionary and assign its value a key.
car_1 = {'manufacturer':'Ford', 'model':'mustang', 'year':'2000'}
car_2 = {'manufacturer':'Toyota', 'model':'corolla', 'year':'2001'}

#Then the script can access a value by the key name 
print(car_1, car_2)
print(car_1['manufacturer'], car_1['model'], car_1['year'])

#This is the basic syntax of a dictionary. 
#In the next lesson, we will explore methods that can be used to work with dictionaries in python. 
