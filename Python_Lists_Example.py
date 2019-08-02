# My Python Lists Example 

""" List is a collection which is ordered and changeable. Allows duplicate members. """

#Create a List

thislist = ["apple", "banana", "cherry"]
print(thislist)

#You access the list items by referring to the index number

print(thislist[1])

#To change the value of a specific item, refer to the index number

thislist[1] = "blackcurrant"
print(thislist)

#You can loop through the list items by using a for loop
for x in thislist:
	print(x) 

#To determine if a specified item is present in a list use the in keyword

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
  
#To determine how many items a list has, use the len() method
print(len(thislist))

#To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange")
print(thislist)

#sorting of the Lists
thislist.sort()

#There are several methods to remove items from a list
#The remove() method removes the specified item
#thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified)
thislist.pop()
print(thislist)

#The del keyword removes the specified index
#del thislist[0]
#print(thislist)

#The del keyword can also delete the list completely:
#thislist = ["apple", "banana", "cherry"]
#del thislist 

#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("--- The list() Constructor ---")
print(" -- It is also possible to use the list() constructor to make a list -- ")

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
