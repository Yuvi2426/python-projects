principal = 0
rate = 0
time = 0
while principal <= 0:
    principal = float(input("Enter a principal amount:"))
    if principal <= 0:
        print("principal amount cant be zero or negative.")
while rate <= 0:
        rate = float(input("enter ammount of rate you want:"))
        if rate <= 0:
                print("rate cant be zero or less.")
while time <=0:
        time = int(input("enter a time period for whch you will like to invest for in years:"))
        if time <= 0:
         print("time cant be equal or less than zero.")

print(principal)
print(time)
print(rate)

total = principal * pow((1 + rate / 100), time)
print(f"the total amount after {time} years is {total:.2f}")

