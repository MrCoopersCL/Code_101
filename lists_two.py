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

