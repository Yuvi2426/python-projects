temp = float(input("enter a temperature:"))
unit = input("enter a unit(celsius or fahrenheit:)")
if unit not in ["celsius","fahrenheit"]:
    print("invalid unit")
elif unit == "celsius":
    temp = temp * 9/5  + 32
    print(f"{temp} F")
elif unit == "fahrenheit":
    temp = (temp - 32) * 5/9
    print(f"{temp} C") 