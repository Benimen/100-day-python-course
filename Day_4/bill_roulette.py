import random
import time
import os

os.system("cls")
friends = ["Bempa", "Kansler", "Smulan", "Terrorist", "John_Pork", "Fläsk_ryttaren"]


print("Bempa, Kansler, Smulan, Terrorist, John_Pork and Fläsk_ryttaren is sharing a meal.")
input("Press any button to continue...")
os.system("cls")
print("They play bill roulette to decide who will pay.")
input("Press any button to continue...")
os.system("cls")
print("3...")
time.sleep(1)
os.system("cls")
print("2...")
time.sleep(1)
os.system("cls")
print("1...")
time.sleep(1)
os.system("cls")
print(f"{random.choice(friends)} will pay the bill")