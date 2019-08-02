# My Python Sets Example 

""" A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets. """

#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset) 

#Note: Sets are unordered, so the items will appear in a random order.

"""You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword."""


#Loop through the set, and print the values:
#Iterate through the items and print the values
for x in thisset:
  print(x) 
  
#Check if "banana" is present in the set:
print("banana" in thisset) 

#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
thisset.add("orange")
print(thisset) 

#To add more than one item to a set use the update() method.
thisset.update(["strawberry", "mango", "grapes"])

print(thisset) 

#To determine how many items a set has, use the len() method.
print(len(thisset))

#To remove an item in a set, use the remove(), or the discard() method.
#Remove "banana" by using the remove() method:
thisset.remove("banana")
print(thisset)

#If the item to remove does not exist, remove() will raise an error.

#Remove "strawberry" by using the discard() method:
thisset.discard("strawberry")
print(thisset) 

#If the item to remove does not exist, discard() will NOT raise an error.

"""You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed."""

#Remove the last item by using the pop() method:
x = thisset.pop()
print(x)
print(thisset) 

#Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

#The clear() method empties the set:
thisset.clear()
print(thisset) 

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
print(thisset) 
del thisset
#print(thisset) 

#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

#Python Set copy() Method :Returns a copy of the set
#Copy the fruits set:

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#Python Set difference() Method : Returns a set containing the difference between two or more sets
#Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z) 

#Python Set difference_update() Method : Removes the items in this set that are also included in another, specified set
#Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

""" The difference_update() method removes the items that exist in both sets.

The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set."""

#Python Set discard() Method : Remove the specified item
#Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) 

""" This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not."""

#Python Set intersection() Method : Returns a set, that is the intersection of two other sets
#Return a set that contains the items that exist in both set x, and set y:
#Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

#Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result) 

#Python Set intersection_update() Method : Removes the items in this set that are not present in other, specified set(s)
#Remove the items that is not present in both x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

"""The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set."""

#Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x) 

#Python Set isdisjoint() Method : Returns whether two sets have a intersection or not
#Return True if no items in set x is present in set y

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)
print(z)

#Python Set issubset() Method : Returns whether another set contains this set or not
#Return True if all items set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) 

#Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z) 

#Python Set issuperset() Method : Returns whether this set contains another set or not
#Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) 

#What if not all items are present in the specified set?
#Return False if not all items in set y are present in set x:

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) 

#Python Set symmetric_difference() Method : Returns a set with the symmetric differences of two sets
#Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) 

#Python Set symmetric_difference_update() Method : inserts the symmetric differences from this set and another
#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 

#Python Set union() Method : Return a set containing the union of sets
#Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) 

"""The union() method returns a set that contains all items from the original set, and all items from the specified sets.

You can specify as many sets you want, separated by commas.

If an item is present in more than one set, the result will contain only one appearance of this item."""

#Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result) 