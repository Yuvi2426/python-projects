name = input("plz enter your first name:")
birth_year = input("Plz enter your birth year(for . eg 2000): ")
name = name.lower()
#print(name)
if len(name) < 3:
    password = name + birth_year[2:4]
    print(password)
else:
    password = name[0:3] + birth_year[2:4]
    print(password)
