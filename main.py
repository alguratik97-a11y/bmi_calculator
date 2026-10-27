# Python program to calculate Body Mass Index (BMI)

# Taking weight in kilograms from the user
weight = float(input("Enter your weight in kg: "))

# Taking height in meters from the user
height = float(input("Enter your height in meters: "))

# Calculating BMI using the formula: weight / (height)^2
bmi = weight / (height ** 2)

# Displaying the calculated BMI
print(f"Your BMI is: {bmi:.2f}")

# Checking BMI categories using conditional statements
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You have a normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
