groceries =[["apple", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    #empty print statement to add a newline after each collection
    print()