#  7. Create a script to reverse a number entered by the user.

print("Enter a number to reverse:")
number = input()
print(f"Reversed Number: {int(number[::-1])}")

#or

print("Enter another number to reverse:")
number = int(input())
reverse_num = 0

while number > 0:
    digit = number%10
    reverse_num = reverse_num * 10 + digit
    number = number//10

print(f"Reversed Number: {reverse_num}")
