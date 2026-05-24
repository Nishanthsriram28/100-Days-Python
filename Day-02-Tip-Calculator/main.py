print("Welcome to the tip Calculator!")
bill = int(input("What was the total bill? $"))
tip_percentage = int(input("How much tip% would you like to give? 10,12 or 15: "))
people = int(input("How many people to split the bill? "))
tip_calculated = (tip_percentage/100)
tip_amount = (bill*tip_calculated)
finalBill = (bill+tip_amount)/people
print(f"Each person should pay: {finalBill}")
