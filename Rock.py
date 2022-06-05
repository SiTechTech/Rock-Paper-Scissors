import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Tie!")
        ties += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Tie!")
        ties += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie!")
        ties += 1

    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times!")
print("You lose", computer_wins, "times")
print("Tie game", ties)
print("________________________________________")
print('''
Thank you for playing
Hope you see you again 
        Peace
''')
print("_________________________________________")
