from calculator import calculate_bmi

while True:
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            break

        except ValueError:
            print("Weight must be a number")
        
    while True:
            
            
        try:
            height = float(input("Enter your height (m): "))
            break

        except ValueError:
            print("Height must be a number")
        s

    
    try:    
        result = calculate_bmi(weight, height)
        print(result)
        break
        
        
    except ValueError as error:
        print(f"Invalid input: {error}")
        print("Please try again.\n")
        