print("Welcome to the tip calculator!")
print("What was the total bill? (in $)")
bill = float(input())
print("How much tip would you like to give? 10, 12, or 15?")
tip = int(input())
print("How many people to split the bill?")
splitters = int(input())
total = bill + ((tip * bill) / 100)
each_share = total / splitters
each_share = round(each_share, 2)
print(f"Each person should pay: ${each_share}")