def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

def length_converter():
    meters = float(input("Enter length in meters: "))
    feet = meters * 3.28084
    print(f"{meters} meters is equal to {feet} feet")

def weight_converter():
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kilograms is equal to {pounds} pounds")

def main():
    print("Choose the conversion type:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
