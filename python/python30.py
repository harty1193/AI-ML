# 30. Write a program to create a basic calculator using if-elif conditions.

print("1. Add\n2. Subtract\n3. Multiply\n4. Division")

option = int(input("Enter the option [1-4]: "))
if option == 1:
    length = int(input("How many numbers you want to Add: "))
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(int(input("How many numbers do you want to add? ")))]
    print("Result after addition: ", sum(numbers))
elif option == 2:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the number to subratract from the first number: "))
    print("Result after subtraction is: ", a-b)
elif option == 3:
    length = int(input("How many numbers you want to Add: "))
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(int(input("How many numbers do you want to add? ")))]
    product = 1
    for i in numbers:
        product *= i
    print("Result after multiplication is: ", product)
elif option == 4:
    a = int(input("Enter the number you want to Divide: "))
    b = int(input("Enter the number you want to Divide with: "))
    if b != 0:
        print("Result after division:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid Option.")
