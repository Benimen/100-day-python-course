print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage would you like to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100) * bill
total_sum = (bill_with_tip + bill) / people
rounded_bill_sum= round(total_sum, 2)

print(f"Each person should pay: ${rounded_bill_sum}")