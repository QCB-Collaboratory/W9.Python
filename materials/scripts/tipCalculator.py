import sys

print(sys.argv)

# Calculates cost of meal with tax and tip
meal = 44.50
tax = 0.075
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)


