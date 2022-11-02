#gooey bar 
def dotbar(x):
    print('.' * int(x))

# Define the raw data

alphabet = ['a','b','c','d','e','f','g']

#obtain length of list
print(f'The length of the {type(alphabet)} is : {len(alphabet)}')
dotbar(50)

#obtain the content of the list
def list_getter():
    print(f'The list content is: {alphabet[:]}')
    for TOM in alphabet:
        print('Type of list item : ', type(TOM))

list_getter()
dotbar(50)

#You can also make a list of lists
list_list = [['a','b','c'],[1,2,3],['doe','ray','me']]
print(f'type of data {type(list_list)} with length {len(list_list)}')
dotbar(50)
print(list_list[:])

#check the type of each list member
for lists in list_list:
    print(type(lists))

#There is now a second index in this nested list
print(list_list[2][:])
dotbar(50)

#Try to see if you can find the pattern 
print(list_list[0])
print(list_list[0][0], list_list[0][1], list_list[0][2])

print(list_list[1])
print(list_list[1][0], list_list[1][1], list_list[1][2])

print(list_list[2])
print(list_list[2][0], list_list[2][1], list_list[2][2])

#This syntax is very important to remember!
#This is because if the wrong index is used then append, insert, and pop can lead to incorrect data. 

#A question might go something like this:
#Remove the first item from the first list, the second item from the second list, and the third item from the third list. 
list_list[0].pop(0)
list_list[1].pop(1)
list_list[2].pop(2)

print(list_list)
dotbar(50)
#here is another on add the string 'name' to the end of each nested list. 
list_list[0].append('name')
list_list[1].append('name')
list_list[2].append('name')

print(list_list)

#As you can see there are many things that can be done with lists. 
#The important thing is to know how the index references an item in the list. 
#This is how you can make sure that the method being run on the list is the correct one. 
