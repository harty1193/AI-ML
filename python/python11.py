#  11. Write a script to calculate simple interest and compound interest.

p = float(input(f"Enter the Principal amount: "))
r = float(input(f"Enter the interset rate in percentage: "))
t = int(input(f"Enter the time in years: "))

si = p*r*t/100

print(f"The simple interest would be {si:.2f}. So the total amount would be {p+si:.2f}.")

n = int(input(f"Enter the Compound Interval (Ex: half yearly = 2, quarterly = 4): "))

ta = p * (pow((1+r/(100*n)),n*t))


print(f"The compound interest would be {ta-p:.2f}. So the total amount would be {ta:.2f}.")
