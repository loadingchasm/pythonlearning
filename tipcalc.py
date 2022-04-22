total_bill = float(input("Welcome to the tip calculator! What was the total bill? $"))
people = float(input("How many people to split the bill? "))
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))

tip_Total = (tipPercentage / 100) + 1
cost = (total_bill / 5) * tip_Total

final_amount = "{:.2f}".format(cost)

print(f"Each person should pay: ${final_amount}")
