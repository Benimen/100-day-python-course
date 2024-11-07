# menu = input("Would you like to see the menu? YES/NO: ")

# ## Menu 
# if menu == "YES" or menu == "yes":
#     print("Pizza Menu:")
#     print("Small pizza: $15")
#     print("Medium pizza: $20")
#     print("Large pizza: $25")
#     print("extra pepperoni for small pizza +$2")
#     print("extra pepperoni for medium or large pizza +$3")
#     print("extra cheese for any size pizza +$1")

# else: menu == "NO" or menu == "no"


# size = input("What size pizza do you want? S, M, or L: ")
# bill = int(0)

# ## Small Pizza
# if size == "s" or size == "S":
#     bill = bill + 15
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "y" or pepperoni == "Y":
#         bill = bill + 2
    
#     else: pepperoni == "n" or pepperoni == "N"
    
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "y" or extra_cheese == "Y":
#         bill = bill + 1


# ## Medium Pizza
# elif size == "m" or size == "M":
#     bill = bill + 20
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "y" or pepperoni == "Y":
#         bill = bill + 3
    
#     else: pepperoni == "n" or pepperoni == "N"
    
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "y" or extra_cheese == "Y":
#         bill = bill + 1


# ## Large Pizza
# elif size == "l" or size == "L":
#     bill = bill + 25
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "y" or pepperoni == "Y":
#         bill = bill + 3
    
#     elif pepperoni == "n" or pepperoni == "N":
#         print()
    
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "y" or extra_cheese == "Y":
#         bill = bill + 1

# else: print("Wrong input try again..")

# print(f"Your total will be: {bill}$")


size = input("Pizza size: S, M or L: ")
pepperoni = input("Do you want pepperoni on pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on pizza? Y or N: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total is {bill}$")

## Two versions of the same assignment