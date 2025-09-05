#  26. Write a program to find the second largest number in a list.

length = int(input("Enter the number of elements in the list: "))
numbers = []
for _ in range(length):
    num = int(input("Enter a number: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
if len(unique_numbers) < 2:
    print("There is no second largest number.")
else:
    unique_numbers.sort()
    print("The second largest number is:", unique_numbers[-2])