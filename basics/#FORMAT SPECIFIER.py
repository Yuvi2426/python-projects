#FORMAT SPECIFIER
PRICE = 490000000232131.99
price = -49.99
PRINT = print
# .2f means no of decimals
# 10 means total width of the string
PRINT(f"the price is {PRICE:.2f}")
print(f"the price is {PRICE:10}")
# < means left align, > means right align, ^ means center align
print(f"the price is {PRICE:<10}")
print(f"the price is {PRICE:>10}")  
print(f"the price is {PRICE:^10}")
# + means show the sign, - means show the sign only for negative numbers, space means show a space for positive numbers and a minus sign for negative numbers
print(f"the price is {PRICE:+}")
print(f"the price is {price:-}")
# , means show the comma as a thousand separator
print(f"the price is {PRICE:,}")

