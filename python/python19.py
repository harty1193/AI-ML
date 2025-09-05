#  19. Write a program to generate a multiplication table for a given number.

num = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    