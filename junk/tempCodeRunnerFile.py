weighting = input(" plz choose a weight system ( kg or pounds):")
weight = float(input("plz enter your weight:"))
if weight<= 0:
    print(" you are weight less ")
elif weighting == "kg":
    print(f" your weight in pounds is { weight* 2.2} lbs")
elif weighting == "pounds":
    print(f"your weight in kg is {weight/2.2} kg")
else:
    print("invalid options")