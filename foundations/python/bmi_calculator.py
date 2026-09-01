
def calculate_bmi(weight, height):
    
    
        
    if weight <= 0:
        return "Weight must be greater than zero"
    if height <= 0:
        return "Height must be greater than zero"


    bmi = round(weight/(height * height), 2) 
    if bmi < 18.5:
        status = "underweight"
    elif bmi <= 24.9:
        status = "normal"
    elif bmi <= 29.9:
        status = "overweight"
    else:
        status = "obese"
  
    return (f"BMI: {bmi}\nStatus: {status} ")



weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

result = calculate_bmi(weight, height)
print(result)
   
