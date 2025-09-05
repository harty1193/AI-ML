#  21. Write a program to sort a list without using the sort() method.

length = int(input("Enter the number of elements in the list: "))
numbers = []

for _ in range(length):
    num = int(input("Enter a number: "))
    numbers.append(num)

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted list:", numbers)
