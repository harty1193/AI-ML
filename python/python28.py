#  28. Write a program to find the sum of all elements in a list.

length = int(input("Enter the length of the list: "))

numbers = []
for _ in range(length):
    num = int(input("Enter a number: "))
    numbers.append(num)
#unique_numbers = list(set(numbers))

total = 0

for i in numbers:
    total += i

print(f"The sum of all the numbers in the list {numbers} is {total}")

# or

print(f"The sum of all the numbers in the list {numbers} is ", sum(numbers))