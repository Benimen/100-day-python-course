# Libraries
import random
import os

# Clear screen
os.system("cls")

# Win count
computer_wins = 0
player_wins = 0


# Dialogue
print("Welcome to the rock paper scissors game.")
print("It is best of 3, good luck!")


while True:
    

    # Player input
    player_choice = input("Choose between (rock, paper, scissors)\n")

    # List
    game_list = ["rock", "paper", "scissors"]

    # Computer input
    computer_choice = random.choice(game_list)


    # Draw
    if player_choice == computer_choice:
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, it's a draw.")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")


    # Rock
    elif player_choice == "rock" and computer_choice == "paper":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You lose.")
        computer_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    elif player_choice == "rock" and computer_choice == "scissors":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You win.")
        player_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")


    # Paper
    elif player_choice == "paper" and computer_choice == "rock":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You win.")
        player_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    elif player_choice == "paper" and computer_choice == "scissors":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You lose.")
        computer_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")


    # Scissors
    elif player_choice == "scissors" and computer_choice == "rock":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You lose.")
        computer_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")

    elif player_choice == "scissors" and computer_choice == "paper":
        os.system("cls")
        print(f"You chose {player_choice} and computer chose {computer_choice}, You win.")
        player_wins += 1
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")


    # Check winner
    if computer_wins == 3:
        os.system("cls")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")
        print("GAME OVER, YOU LOSE!")
        break

    # Check winner
    if player_wins == 3:
        os.system("cls")
        print(f"Current scores: computer: {computer_wins} player: {player_wins}")
        print("YOU WIN!")
        break