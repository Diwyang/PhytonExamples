# My Python Conditions and If statements Example 

""" Python has two primitive loop commands:

    while loops
    for loops
 """

#With the while loop we can execute a set of statements as long as a condition is true.
#Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
  
#Note: remember to increment i, or else the loop will continue forever.

#With the break statement we can stop the loop even if the while condition is true:
#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result