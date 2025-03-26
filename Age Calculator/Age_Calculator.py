from datetime import datetime

def age_calculator():
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"You are {age} years old!")

age_calculator()
