print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $ "))
tip_amount = int(input("How much would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
total_sum = (total + tip_amount) / number_of_people
rounded_sum = round(total_sum, 2)
print(f"Each person should pay: ${rounded_sum}")