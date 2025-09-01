# 8. Write a program to find the largest of three numbers.

numbers = [int(input(f"Enter number {i+1}:\t")) for i in range(3)]
numbers.sort()
print(f"The largest number is {numbers[-1]}")