#  5. Write a program to check if a given string is a palindrome.

print("\nLets check if a string is palindrome")
print("------------------------------------\n")
print("Enter a string to check if it is palindrome:")
st = str(input())

if st==st[::-1]:
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")