# My Python Dictionaries Example 

""" A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values. """

#Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Get the value of the "model" key:
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
#Get the value of the "model" key:
x = thisdict.get("model")
print(x)

#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x) 
  
#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x]) 
  
#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x) 
  
#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y) 

#Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  
#Print the number of items in the dictionary:
print(len(thisdict)) 

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)

#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 

#The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

#The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists. 

#The clear() keyword empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

#It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

#Python Dictionary copy() Method : Returns a copy of the dictionary
#Copy the car dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x) 

#Python Dictionary fromkeys() Method : Returns a dictionary with the specified keys and values
#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

#Same example as above, but without specifying the value:
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

#Python Dictionary items() Method : Returns a list containing the a tuple for each key value pair
#Return the dictionary's key-value pairs:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x) 

#When an item in the dictionary changes value, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
car["year"] = 2018
print(x) 

#Python Dictionary keys() Method : Returns a list containing the dictionary's keys
#Return the keys:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) 

#When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
car["color"] = "white"
print(x) 

#Python Dictionary pop() Method : Removes the element with the specified key
#Remove "model" from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car) 

#The value of the removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")
print(x) 

#Python Dictionary popitem() Method :Removes the last inserted key-value pair
#Remove the last item from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car) 

#The removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x) 

#Python Dictionary setdefault() Method : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x) 

#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x) 