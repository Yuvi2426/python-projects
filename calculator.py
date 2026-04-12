operator = input("enter a operator (+,-,*,/): ")
num1 = float(input("enter your first number:"))
num2 = float(input("enter your second number:"))
if operator == "+":
    print(f"your sum is {num1 + num2}")
elif operator == "-":
    print(f"your subtraction is {num1 - num2}")
elif operator == "*":
    print(f"your multiplication is {num1 * num2}")
elif operator == "/":
    print(f"your division is {num1 / num2}")
else:
    print("choose a valid operator")
