#  1. Write a program to swap two variables without using a third variable.

print(f"Enter value for A(string)")
a = input()
print(f"Enter value for B(string)")
b = input()

a,b = b,a

print(f"The Value of A: {a}\nThe value of B: {b}")

#or

print(f"Enter value for X(Integer)")
x = int(input())
print(f"Enter value for Y(Integer)")
y = int(input())

x = x * y
y = x // y
x = x // y

print(f"The Value of x: {x}\nThe value of y: {y}")
