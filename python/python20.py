#  20. Write a script to print all even numbers between 1 and 100.

print("Even numbers between 1 and 100:")
for num in range(1, 101):
    if num % 2 == 0:
        print(num, end=' ')