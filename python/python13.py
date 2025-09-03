#  13. Write a program to find the sum of digits of a number.

number = input("Enter a number: ")
total = 0

if number.isnumeric():
    for i in number:
        total += int(i)
    print(f"The sum of all the digit in {number} is {total}")
else:
    print("This is not a number")

#or

number = int(input("Enter another number: "))
num = number
total = 0
while number > 0:
    a = number % 10
    total += a
    number //= 10
print(f"The sum of all the digit in {num} is {total}")
    
#or (Here it takes the input even if it is alphanumeric.

number = input("Enter another number: ")
total = sum(int(i) for i in number if i.isnumeric())
print(f"The sum of all the digit in {number} is {total}")