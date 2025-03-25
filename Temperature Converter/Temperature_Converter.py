def convert_temp():
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()
    temp = float(input("Enter temperature: "))

    if choice == 'C':
        converted = (temp - 32) * 5/9
        print(f"{temp}°F = {converted:.2f}°C")
    elif choice == 'F':
        converted = (temp * 9/5) + 32
        print(f"{temp}°C = {converted:.2f}°F")
    else:
        print("Invalid choice!")

convert_temp()
