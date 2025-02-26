def length_converter(value, from_unit, to_unit):
    length_units = {
        "meter": 1.0,
        "kilometer": 0.001,
        "centimeter": 100.0,
        "millimeter": 1000.0,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "kilogram": 1.0,
        "gram": 1000.0,
        "pound": 2.20462,
        "ounce": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value  # If units are the same

def main():
    print("Unit Converter")
    print("1. Length\n2. Weight\n3. Temperature")
    choice = input("Select conversion type (1-3): ")
    
    if choice == "1":
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (meter, kilometer, centimeter, etc.): ").lower()
        to_unit = input("Enter to unit: ").lower()
        print(f"Converted Value: {length_converter(value, from_unit, to_unit)} {to_unit}")
    
    elif choice == "2":
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (kilogram, gram, pound, ounce): ").lower()
        to_unit = input("Enter to unit: ").lower()
        print(f"Converted Value: {weight_converter(value, from_unit, to_unit)} {to_unit}")
    
    elif choice == "3":
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("Enter to unit: ").lower()
        print(f"Converted Value: {temperature_converter(value, from_unit, to_unit)} {to_unit}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
