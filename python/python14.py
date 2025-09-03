#  14. Create a script to calculate the square and cube of a number.

def squarefn(num: int):
    return num**2
    
def cubefn(num: int):
    return num**3

number = int(input("Enter a number: "))

square = squarefn(number)
cube = cubefn(number)

print(f"The square is {square} and cube is {cube}")

#Without type casting.

def squarefnx(num):
    if num.isnumeric():
        return int(num)**2
    else:
        print("Not a number")
    
def cubefnx(num):
    if num.isnumeric():
        return int(num)**3
    else:
        print("Not a number")

number = input("Enter a number: ")

square = squarefnx(number)
cube = cubefnx(number)

if square is not None and cube is not None:
    print(f"The square is {square} and cube is {cube}")