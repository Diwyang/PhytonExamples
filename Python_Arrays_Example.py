# My Python Arrays Example 

#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

""" Arrays are used to store multiple values in one single variable:.
An array is a special variable, which can hold more than one value at a time.
 """

#You refer to an array element by referring to the index number
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

#Modify the value of the first array item:
cars[0] = "Toyota" 
print(cars)

#Use the len() method to return the length of an array (the number of elements in an array).
#Return the number of elements in the cars array:
x = len(cars) 
print(x)

#You can use the for in loop to loop through all the elements of an array.
#Print each item in the cars array:
for x in cars:
  print(x) 
  
#Add one more element to the cars array:
cars.append("Honda") 
print(cars)

#You can use the pop() method to remove an element from the array.
#Delete the second element of the cars array:
cars.pop(2) 
print(cars)

#You can also use the remove() method to remove an element from the array.
#Delete the element that has the value "Volvo":
cars.remove("Volvo") 
print(cars)