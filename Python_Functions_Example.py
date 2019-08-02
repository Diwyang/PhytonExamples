# My Python Functions Example 

""" A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
 """

#In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function") 
  
#To call a function, use the function name followed by parenthesis:
my_function() 

#Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

#The following example has a function with one parameter (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 


#The following example shows how to use a default parameter value.
#If we call the function without parameter, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#To let a function return a value, use the return statement:

def my_function1(x):
  return 5 * x

print(my_function1(3))
print(my_function1(5))
print(my_function1(9)) 

#Python also accepts function recursion, which means a defined function can call itself.
#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)