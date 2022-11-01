# A list is assigned a name just like a variable.
candy_bag = ['snickers','peanut butter cup', 'apple']

# A list has the type 'list'
print('cand_bag is a : ', type(candy_bag))

#A list has members which are objects in python
#These members are called ordinal numbers
print('List item one: ', candy_bag[0])
print('List item two: ', candy_bag[1])
print('List Item three: ', candy_bag[2])

#Lets see the length of the list
print('The list length is: ', len(candy_bag))

print('>'*50)
#ordinal numbers can count backwards as well
print('The last list item is: ', candy_bag[-1])
print('The second from lat item is:', candy_bag[-2])
print('The third from last item is: ', candy_bag[-3])

#you may also count over a range of numbers to retrieve members.
print(candy_bag[0:2])
print('>'*50)

#print all members of a list this way
print(candy_bag[:])

#Add a member to a list using the append method
candy_bag.append('butter finger') 
print(candy_bag)

print('>'*50)
#To insert an item at a specific location on the index use the insert method
candy_bag.insert(1, "Tootsie roll")
print(candy_bag)

#an item can also be removed from a list
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('The type of data is: ', type(integer_list))
print('Length of list before remove: ', len(integer_list))

#remove an item
integer_list.remove(3)
print('Length of list after remove: ', len(integer_list))

#the pop nethod can also be used in order to remove at a specific index
integer_list_2 = [1, 2, 3, 4, 5]
print('before pop: ', integer_list_2)
integer_list_2.pop(3)
print('after pop : ', integer_list_2)
print('>' * 50)
#The clear method will remove all members of the list
boolean_list = [True, False, True, True]
print('List before clear: ', boolean_list)
boolean_list.clear()
print('List after the clear :', boolean_list)