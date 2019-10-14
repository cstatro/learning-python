from random import choice

ai = choice(['rock', 'paper', 'scissors'])

user_choice = input('please select rock,paper,or scissors: ')

if ai == user_choice:
    print('its a tie!')
elif user_choice == 'rock' and ai == 'paper':
    print("AI wins")
elif ai == 'rock' and user_choice == 'paper':
    print("user wins")
elif user_choice == 'scissors' and ai == 'paper':
    print('user wins')
elif user_choice == 'paper' and ai == 'scissors':
    print('AI wins')
elif user_choice == 'scissors' and ai == 'rock':
    print('AI wins')
elif ai == 'scissors' and user_choice == 'rock':
    print('user wins')
else:
    print('invalid input')
