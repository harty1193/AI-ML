# Write a program to print the ASCII value of each character in a string.

string = input("Enter a string: ")
for char in string:
    print(f"ASCII value of '{char}' is {ord(char)}")