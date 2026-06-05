# Shopping cart program
print("Welcome to the super market!")
food = []
price = []
quantity = []
food = food.append(input("Enter the name of the food item:"))
price = price.append(float(input("What is the price of food you want to buy?")))
quantity = quantity.append(int(input("How many items have you bought")))
print(f"Your shopping cart currently has {food} with the price of {price} and quantity of {quantity}")
options = input("would yu like to add more item(click y) or quit(use q to quit)")
while True:
    print(f"Your shopping cart currently has {food} with the price of {price} and quantity of {quantity}")
    total = price * quantity
    print(f"The total price of your shopping cart is {total}")
    break
else:
    food = food.append(input("Enter the name of the food item:"))
    price = price.append(float(input("What is the price of food you want to buy?")))
    quantity = quantity.append(int(input("How many items have you bought")))
    print(f"Your shopping cart currently has {food} with the price of {price} and quantity of {quantity}")
    options = input("would yu like to add more item(click y) or quit(use q to quit)")
