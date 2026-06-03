bill = float(input("how much was your bill?"))
people = int(input("how many people were in your dinner?"))
tip = float(input("how much percent are you guys going to tip %?"))
tip = bill * tip / 100
bill = tip + bill
bill_per_person = bill / people
print(f"each of us have to put ${bill_per_person:.2f} for an equal contribution.")

leftover_pennies = bill - bill_per_person 
if leftover_pennies <= 0:
 print("bill was equally split")
else:
  print(f"i will be paying the remaining {leftover_pennies:.2f} by myself ")

