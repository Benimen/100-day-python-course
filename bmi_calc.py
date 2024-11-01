height = float(input("What's your height?")) / 100
weight = int(input("What's your weight?"))

BMI = weight / (height * height)
rounded_BMI = round(BMI, 2)

if rounded_BMI <= 18.28:
    print(f"Your rounded_BMI is {rounded_BMI}, you are underweight")
elif (rounded_BMI > 18.28) and (rounded_BMI <= 22.0):
    print(f"Your rounded_BMI is {rounded_BMI}, slightly underweight")
elif (rounded_BMI > 22.0) and (rounded_BMI <= 28.50):
    print(f"Your rounded_BMI is {rounded_BMI}, you are normal weight")
elif (rounded_BMI > 28.50) and (rounded_BMI <= 32.56):
    print(f"Your rounded_BMI is {rounded_BMI}, you are obese")
else:
    print(f"Your rounded_BMI is {rounded_BMI}, talk to a doctor")
