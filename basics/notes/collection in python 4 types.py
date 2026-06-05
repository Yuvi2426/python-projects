# collecton in python 4 types
#  list - []
#for more than one value use list
#fruits = ["coconut","apple","orange","banana"]
# to gain any one use index operator 0,1,2,3 and much more
#print(fruits[0])
#print(fruits[1])    
#print(fruits[2])
# to gain the last one use -1
#print(fruits[::-1])

#for i in fruits:
 #   print(i)

# to check wheather a fruit is in or not use
#print("apple" in fruits)
# it states wheather true or ga;se  

#print("grapes" in fruits)

#fruits[0] = "grapes"

#fruits.remove("grapes")

#to add a fruit at specific index use insert
#fruits.insert(0,"grapes") 

# use sort for alphabetical order
# to reverse the order use reverse
#fruits.sort()   
# clear means to remove all the items in the list
# index for no of items in the list
#print(fruits.index("grapes"))
# count for no of times a fruit is in the list


#fruits.append(  "grapes")
#len(fruits)
#print(fruits)



# set - {}
#fruits_set = {"coconut", "apple", "orange", "banana"}
# most of the commands are same as list but the order is not maintained and it does not allow duplicates
#indexing is not allowed in set and it does not maintain the order of items
# add to add and remove to remove a fruit from the set
#fruits_set.add("grapes")
# pop to remove a random item from the set
#fruits_set.pop()
#print(fruits_set) 

# tuple - ()
fruits_tuple = ("apple","coconut", "apple", "orange", "banana")
# it is immutable and does not allow duplicates
# indexing is allowed in tuple and it maintains the order of items
print(fruits_tuple.count("apple")) 