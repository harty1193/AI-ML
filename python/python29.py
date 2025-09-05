#  29. Write a script to check if a substring is present in a string.

string = input("Enter a string: ")
sub_string = input("Enter a sub string: ")

print("The substring is present in the string." if sub_string in string else "The substring is not present in the string.")