# A basic Game Script

#Title: Sir Pythons Quest
#genre: fantasy
#setting: Battlefield
#First person perspective

#Prompt number 1
print('''
Ye have arrived upon a great battlefield.
Smoke and fire can be seen rising from far
across the grass. Your quest is to slay
the bone gore monger.
------------------------------------------
''')

print('''
------------------------------------------
Decisions:
1. run away
2. use spy glass
3. check map
4. run forward
------------------------------------------
''')
decision_1 = input('What is thy decision?')

if decision_1 == '1':
    print('You run away like a little baby. Everyone laughs and you cry. Nice!')
elif decision_1 == '2':
    print('You look through your spyglass and see the bone gore monger feasting upon raw human flesh.')
elif decision_1 == '3':
    print('As you check your map, someone shouts out "NERD!".')
elif decision_1 == '4':
    print('You run forward, shouting your battle cry at the top of your lungs.')
else:
    print('I didnt quite understand that, try again?')


