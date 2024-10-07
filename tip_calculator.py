print("Welcome to Tip Calculator Program")

bill = float(input("How much is the bill: $"))
tip = int(input("How many percent of the tip amount: "))
person = int(input("How many people: "))

bill_amount = round(bill + (bill * tip / 100), 2)
total_bill = round(bill_amount / person, 2)

print(f"Total bill: ${bill_amount}\nEach person has to pay: ${total_bill}")