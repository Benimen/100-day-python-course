# Libraries
import random
import os

# Clear screen function
def clear_screen():
    os.system("cls")

# Win count
computer_wins = 0
player_wins = 0

# Calls clear screen function
clear_screen()

# Dialogue
print("Welcome to the rock paper scissors game.")
print("It is best of 3, good luck!")
input("Press any button to continue...")

# Calls clear screen function
clear_screen()

# Winning combination Dictionary
winning_combinations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    

    # Player input
    player_choice = input("Choose between (rock, paper, scissors)\n").lower()
    if player_choice not in winning_combinations:
        clear_screen()
        print(f"{player_choice} is a invalid choice, try again.")
        continue

    # Computer input
    computer_choice = random.choice(list(winning_combinations.keys()))

    # Check result
    if player_choice == computer_choice:
        clear_screen()
        print(f"You chose {player_choice}, and the computer chose {computer_choice}, it's a draw.")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    elif winning_combinations[player_choice] == computer_choice:
        player_wins += 1
        clear_screen()
        print(f"You chose {player_choice}, and the computer chose {computer_choice}")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    else:
        computer_wins += 1
        clear_screen()
        print(f"You chose {player_choice}, and the computer chose {computer_choice}")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    # Check winner
    if computer_wins == 3:
        print("GAME OVER, YOU LOSE!")
        break

    # Check winner
    if player_wins == 3:
        print("YOU WIN!")
        break