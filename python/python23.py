#  23. Write a program to remove duplicates from a list.

length = int(input("Enter the number of elements in the list: "))
numbers = []
for _ in range(length):
    num = int(input("Enter a number: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)