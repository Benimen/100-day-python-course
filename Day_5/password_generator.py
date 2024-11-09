#Password Generator Project
import random
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


letters = random.choices(letters, k=nr_letters)
numbers = random.choices(numbers, k=nr_numbers)
symbols = random.choices(symbols, k=nr_symbols)


new_password = letters + numbers + symbols
random.shuffle(new_password)
final_password = "".join(new_password)

os.system("cls")

length = len(final_password)
if length < 10:
    print(f"Length of password is {length}, password is weak")
elif length >= 10 and length <= 14:
    print(f"Length of password is {length}, password is good")
elif length > 14 and length < 50:
    print(f"Length of password is {length}, password is strong.")
elif length >= 50:
    print("Password is too long")
    exit()


print(f"Your new password is: \n{final_password}")
