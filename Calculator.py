#Simple Calculator

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
choice = input("Calculator \n 1.Multiplication \n 2. Division \n 3. Subtraction \n 4. Addition \n Enter your choice: ")

if choice == "1":
    print(f"The results are:{x * y}")
elif choice == "2":
    print(f"The results are:{x / y} ")
elif choice == "3":
    print(f"The results are:{x - y}")
elif choice == "4":
    print(f"The results are:{x +y}")
else:
    print("Invalid Input.")
