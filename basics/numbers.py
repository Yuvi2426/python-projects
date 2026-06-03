num = int(input("enter a number: " ))
if num>0:
    print(f"{num} is a positive number")
elif num<0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")

    
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

if num>1000:
    print(f"{num} is a larger number")
elif 1000>num>100:
    print(f"{num} is a medium number")
elif num<100:
    print(f"{num} is a smaller number")




