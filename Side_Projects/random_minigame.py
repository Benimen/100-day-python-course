import random
import os

random_number = random.randrange(1, 11)
feedback = ""

while True:

    # Clear the screen
    os.system("cls")

    # Display feedback from the last guess
    if feedback:
        print(feedback)


    # Get input from user
    number = input("Guess the number from [1 - 10]: ")


    # Check if input is a integer
    if number.isdigit():
        number = int(number)

        # Check if the guess is correct
        if number == random_number:
            print(f"The correct number was {random_number}, YOU WON!!")
            break
        elif number < 1 or number > 10:
            feedback = "Please be in range"
    else:
        feedback = "Please enter a integer"