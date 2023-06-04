print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? (In %age) "))

people = int(input("How many people to split the bill? "))

total_bill_with_tip = total_bill * (1 + tip / 100)
bill_per_person = total_bill_with_tip  / people

# You can also do round(bill_per_person, 2) but that'd
# loose accuracy when working too
print("Each person should pay: ${:.2f}".format(bill_per_person))