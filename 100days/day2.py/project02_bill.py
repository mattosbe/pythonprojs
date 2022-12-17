print("Welcome to the tip calculator")
total_bill = float(input("What was your total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_split = float(input("How many people to split the bill? "))
tip = (tip_percentage/100) * (total_bill/people_split)
bill_tip = (total_bill/people_split) + tip 
bill_tip = str(round(bill_tip, 2))
print(f"Each person should pay: {bill_tip}")