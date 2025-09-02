# 12. Write a program to check if a number is prime or not.

number = int(input(f"Enter a number to check prime or not: "))
if number < 1:
    print("Not a Prime")
else:
    prime = True
    for i in range(2,int(number**.5)+1):
        if not (number % i):
            print("Not a Prime number")
            prime = False
            break
    if prime:
        print("{number} is a Prime number")