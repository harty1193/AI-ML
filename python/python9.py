# 9. Write a program to count vowels and consonants in a string.

string = input(f"Enter a string: ")
v_count = 0
c_count = 0

for letter in string:
    if letter.isalpha():
        if letter in "aeiouAEIOU":
            v_count += 1
        else:
            c_count += 1

print(f"Total count of consonants is {c_count} and vowels {v_count}")