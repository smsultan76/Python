while 1:
    print("Choose the conversion type: \n    1. Celsius to Fahrenheit \n    2. Fahrenheit to Celsius \n    3. Exit")
    choise = int(input("Enter your choise: "))
    if choise == 1:
        Celsius = float(input("Enter the temperature in Celsius: "))
        Fahrenheit = (Celsius * 9/5) + 32
        print(f"The temperature in Fahrenheit is: {Fahrenheit}\n")
    elif choise == 2:
        Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5/9
        print(f"The temperature in Celsius is: {Celsius}\n")
    elif choise == 3:
        break