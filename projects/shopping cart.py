# shopping cart program working with lists
foods =[]
prices = []
total = 0

while True:
    food = input("Enter the food you would like to buy (or q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food $ "))
        foods.append(food)
        prices.append(price)
        
print("'Your shopping cart:")
for food in foods:
    print(food)
 
for price in prices:
    total = total + price
    print(price)

print(f"Your total is ${total:.2f}")