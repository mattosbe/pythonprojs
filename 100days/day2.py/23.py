age = int(input("What is your current age? "))
age_days = (age - 90) * 365
age_weeks = (age - 90) * 52
age_months = (age - 90) * 12
print(f"You have {abs(age_days)} days, {abs(age_weeks)} weeks, and {abs(age_months)} months left.")