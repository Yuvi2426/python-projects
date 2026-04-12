import math
base = float(input("Enter the base of the triangle: "))
perperdicular = float(input("Enter the perpendicular of the triangle: "))
hypotenuse = math.sqrt(pow(base, 2) + pow(perperdicular, 2))
print("The hypotenuse of the triangle is: ", hypotenuse)