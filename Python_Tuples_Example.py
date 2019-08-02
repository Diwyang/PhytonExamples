# My Python Tuples Example 

""" A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. """

#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#You can access tuple items by referring to the index number, inside square brackets

print(thistuple[1])

#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#You cannot change values in a tuple:

#thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

#Loop Through a Tuple
#Iterate through the items and print the values
for x in thistuple:
  print(x) 
  
#To determine if a specified item is present in a tuple use the in keyword:
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#To determine how many items a tuple has, use the len() method
print(len(thistuple)) 

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#thistuple[3] = "orange" # This will raise an error
print(thistuple)

#Note: You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists 

#It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Return the number of times the value 5 appears in the tuple:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#Search for the first occurrence of the value 8, and return its position
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)