print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("There is a secret ending in this game, try to find it IF you can, see what i did there.")
choice1 = input("Choose which way to go: [left] or [right]: ").lower()

if choice1 == "right":
    print("You fell into a hole, GAME OVER.")

elif choice1 == "left":
    print("You've arrived at a lake")
    choice2 = input("Choose to [wait] for a boat or [swim]: ").lower()
    
    if choice2 == "right":
        print("You forgot that you can't swim, GAME OVER")
    
    elif choice2 == "wait":
        print("You've encountered three doors, a pink, red, and black")
        choice3 = input("Choose which door to go through, [pink] [red] [black]: ").lower()
        
        if choice3 == "pink":
            print("You opened the door and got shot in the face by a trap.")
            print("GAME OVER")
        
        elif choice3 == "red":
            print("You opened the red door and got barbecued by a flamethrower, what did you expect?")
            print("GAME OVER")
        
        elif choice3 == "black":
            print("You opened the door and found a small chest with treasure in it.")
            print("YOU WON!!")

        elif choice3 == "secret ending":
            print("You found the secret ending!")