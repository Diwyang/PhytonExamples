# My Example 7
""" Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

	"""

print("--- Python Arithmetic Operators ---")
	
x = 3;
y = 5;

print("---x+y ----")

print(x+y)

print("-- x-y --")

print(x-y)

print("-- x*y --")

print(x*y)

print("-- x/y --")

print(x/y)

print("-- x%y --")
print(x%y)

print("--	x**y --")
print(x**y)

print("-- x//y --")
print(x//y)


print("--- Python Assignment Operators ---")

print("-- x=5 --")
x=5
print(x)

print("-- x+=3 --")
x+=3
print(x)

print("-- x-=3 --")
x-=3
print(x)

print("-- x*=3 --")
x*=3
print(x)

print("-- x/=3 --")
x/=3
print(x)

print("-- x%=3 --")
x%=3
print(x)

print("-- x//=3 --")
x//=3
print(x)

print("-- x**=3 --")
x**=3
print(x)

x=5
print(x)
print("-- x&=3 --")
x&=3
print(x)

x=5
print(x)
print("-- x|=3 --")
x|=3
print(x)

x=5
print(x)
print("-- x^=3 --")
x^=3
print(x)

x=5
print(x)
print("-- x>>=3 --")
x>>=3
print(x)

x=5
print(x)
print("-- x<<=3 --")
x<<=3
print(x)


print("--- Python Logical Operators ---")

x = 5
print("-- x > 3 and x < 10 --")
print(x > 3 and x < 10)

print("-- x > 3 or x < 4 --")
print(x > 3 or x < 4)

print("-- not(x > 3 and x < 10) --")
print(not(x > 3 and x < 10))


print("--- Python Identity Operators ---")
print(" --- is not operator ---")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

#print(x <> y)

# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y

print(" --- is  operator ---")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print("--- Python Membership Operators ---")

print(" --- in  operator ---")

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print(" --- not in  operator ---")

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list