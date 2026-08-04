#Conversion of Temperature Between Celsius and Kelvin
#K = C + 273
#C = K + 273
#Conversion of Temperature Between Fahrenheit and Celsius
#C = (F-32) X 5/9
#F = C(9⁄5) + 32
#Conversion of Temperature Between Fahrenheit and Kelvin
#K = (F − 32) × 5⁄9 + 273.15
#F = (K – 273.15) × 9⁄5 + 32

choice = input("*Temparature Converter* \n 1.Celcius (Kelvin/Fahrenheit) \n 2.Farenheit (Kelvin/Celcius) \n 3.Kelvin (Fahrenheit/Celcius) \n Choose your Option: ")


if choice == "1":
    print("You choosed Celcius")
    option = int(input("Choose from the Options below \n 1.Kelvin \n 2.Fahrenheit \n Please Input your choice: "))
    if option == 1:
        print("You chose Celcius - Kelvin")
        C = float(input("How many Celcius: "))
        K = C + 273.15
        print(f"Therefore, {C}°C = {K}°K")
    elif option == 2:
        print("You chose Celcius - Fahrenheit ")
        Celcius = float(input("How many Celcius: "))
        Result1 = 9/5
        Result2 = Result1 * Celcius
        F = Result2 + 32
        print(f"Therefore, {Celcius}°C = {F} Fahrenheit")
elif choice =="2":
    print("You chosed Farenheit")
    option = int(input("Choose from the options below \n 1.Kelvin \n 2.Celcius \n Please input your choice: "))
    if option == 1:
        print("You chose Fahrenheit - Kelvin")
        F = float(input("How many Fahrenheit: "))
        Result1 = F - 32 
        Result2 = 5/9 
        Result3 = Result2 * Result1
        K = Result3 + 273.15
        print(f"Therefore, {F}°F = {K}°K")
    elif option == 2:
        print("You chose Fahrenheit - Celcius")
        F = float(input("How many Fahrenheit: "))
        Result1 = F - 32 
        Result2 = 5/9 
        C = Result2 * Result1
        print(f"Therefore, {F}°F = {C}°C")
elif choice == "3": 
    print("You chose Kelvin")
    option = int(input("Choose from the options below \n 1.Fahrenheit \n 2.Celcius \n Please input your choice: "))
    if option == 1:
        print("You chose Kelvin - Fahrenheit")
        K = float(input("How many Kelvin: "))
        Result1 = K - 273.15
        Result2 = 9/5
        Result3 = Result1 * Result2
        F = Result3 + 32
        print(f"Therefore, {K}°k = {F}°F")
    elif option == 2:
        print("You chose Kelvin - Celcius")
        K = float(input("How many Kelvin: "))
        C = K - 273.15
        print(f"Therefore, {K}°k = {C}°C")
