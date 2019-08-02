# My Example 6
""" String literals in python are surrounded by either single quotation marks, or double quotation marks."""

print("----Get the character at position 1 (remember that the first character has the position 0)----")

a = "Hello, World!"
print(a[1])

print("--Substring. Get the characters from position 2 to position 5 (not included)--")

b = "Hello, World!"
print(b[2:5])

print("--The strip() method removes any whitespace from the beginning or the end --")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

print("-- The len() method returns the length of a string --")

a = "Hello, World!"
print(len(a))

print("--The lower() method returns the string in lower case --")
print(a.lower())

print("--The upper() method returns the string in upper case --")
print(a.upper())

print("--The replace() method replaces a string with another string --")
print(a.replace("H", "J"))

print("-- The split() method splits the string into substrings if it finds instances of the separator --")
print(a.split(",")) # returns ['Hello', ' World!'] 