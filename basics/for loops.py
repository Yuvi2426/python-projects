# reverse means to start from the end and go to the beginning. in this case, we are counting down from 10 to 1.
#for x in reversed(range(1, 11)):
# range works from the no you start fro and ends from the end no
#2 signifies to count by 2s. so it will count 1, 3, 5, 7, 9
#for x in reversed(range(1, 11, 2)):
#for x in (range(1, 11)):
   # print(x)

#print("happy new year!")
#credit = "1234-1231-1331-1231"
#for x in credit:
  #  print(x)

# continue is used to skip a certain part of the code. in this case, we are skipping the number 5
for x in range(1,100):
    if x == 5 or x == 10:
        continue
    print(x)

#break 
for x in range(1,100):
    if x == 5 or x == 10:
        break
    print(x)
