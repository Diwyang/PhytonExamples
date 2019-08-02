# My Python Conditions and If statements Example 

""" Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops. """

#An "if statement" is written by using the if keyword.
#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print("hello")
else:
  print("a is greater than b")

#If you have only one statement to execute, you can put it on the same line as the if statement.
#One line if statement:
if a > b: print("a is greater than b")

#One line if else statement:
print("A") if a > b else print("B") 

#One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B") 

#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")
  
#The or keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, OR if a is greater than c:

if a > b or a > c:
  print("At least one of the conditions is True")
  
