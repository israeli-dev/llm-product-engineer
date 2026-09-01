from calculator import calculate_bmi


weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

result = calculate_bmi(weight, height)

print(result)