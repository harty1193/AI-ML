# 10. Create a program that prints the Fibonacci series up to n terms.

# Program to print Fibonacci sequence up to 20

prv, nxt = 0, 1
n = int(input(f"Enter a value for n: "))
while prv <= n:
    print(prv, end='  ')
    prv,nxt = nxt, prv + nxt

#or

prv = 0   
nxt = 1
n = int(input(f"\nEnter another value for n: "))

while prv <= n:
    print(prv, end='  ')
    tmp = prv + nxt
    prv = nxt
    nxt = tmp