#  27. Write a script to create a dictionary with numbers and their squares from 1 to n

n = int(input("Enter the number: "))

numbers = []
squares = []

for i in range(1,n+1):
    numbers.append(i)
    squares.append(i*i)

merged_dict = {}
for i in range(0,n):
    merged_dict[numbers[i]] = squares[i] 

print(f"Dictionary with numbers and their squares from 1 to {n}:", merged_dict)