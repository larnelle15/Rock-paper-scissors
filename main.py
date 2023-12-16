import random

player_wins = 0
cpu_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_choice == "q":
        break

    if player_choice not in options:
        continue

    cpu_choice = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[cpu_choice]
    print("Computer picked", computer_pick + ".")

    if player_choice == "rock" and cpu_option == "scissors":
        print("You got it!")
        user_wins += 1

    elif player_choice == "paper" and cpu_option == "rock":
        print("You got it!")
        user_wins += 1

    elif player_choice == "scissors" and cpu_option == "paper":
        print("You got it!")
        user_wins += 1

    else:
        print("You lost!")
        cpu_wins += 1

print("Main player wins", player_wins, "times.")
print("The computer wins", cpu_wins, "times.")
print("See you Later!")
