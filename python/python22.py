#  22. Write a program to merge two lists into a dictionary (one as keys, one as values).

number_keys = int(input("Enter the number of keys: "))
number_values = int(input("Enter the number of values: "))
keys = []
values = []
for i in range(number_keys):
    key = input(f"Enter key {i+1}: ")
    keys.append(key)

for j in range(number_values):
    value = input(f"Enter value {j+1}: ")
    values.append(value)

merged_dict = dict(zip(keys, values))
print("Merged dictionary:", merged_dict)

# or

# Using dictionary comprehension
merged_dict = {k: v for k, v in zip(keys, values)}
print("Merged dictionary:", merged_dict)

#or

# Using a loop
merged_dict = {}
for i in range(min(len(keys), len(values))):
    merged_dict[keys[i]] = values[i] 
print("Merged dictionary:", merged_dict)