#  6. Write a program to calculate the factorial of a number.

print("Lets calculate factorial of a number")
print("Enter a number:")
num = int(input())
factorial = num

for n in range(1,num-1):
    factorial *= num-n
                
print(f"Factorail of {num} is {factorial}")
        