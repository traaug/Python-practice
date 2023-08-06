import random

print("This is rock,paper,scissor GAME")
player_name = input("Enter your name: ")
print("Welcome to the game, {}".format(player_name))
items = ['rock','paper','scissor']
player_input = input("enter your choice: rock, paper or scissor? ").lower()
while player_input not in items:
    print("you can only add rock,paper or sicssor! please enter again.")
    player_input = input("enter your choice: rock, paper or scissor? ").lower()

while player_input != 'off':
    computer_choice = random.choice(items)
    print("Computer choice is: {}".format(computer_choice))

    if player_input == computer_choice:
        print("Draw")

    elif player_input == 'rock':
        if computer_choice == 'paper':
            print("I am sorry, computer wins.")
        elif computer_choice == 'scissor':
            print("Congratulations! you wins.")

    elif player_input == 'paper':
        if computer_choice == 'scissor':
            print("I am sorry, computer wins.")
        elif computer_choice == 'rock':
            print("Congratulations! you wins.")

    elif player_input == 'scissor':
        if computer_choice == 'rock':
            print("I am sorry, computer wins.")
        elif computer_choice == 'paper':
            print("Congratulations! you wins.")

    player_input = input("enter your choice: rock, paper or scissor? ").lower()

"""
if you dont want other to see the input, 
you can use getpass.getpass in the place of input
"""
