'''
03/08/2021

Review

List
mutable, []

List functions

  LIST.insert(INDEX, ELEMENT)
  LIST.append(ELEMENT)
  LIST.remove(ELEMENT)
  LIST.pop(INDEX)

LIST[INDEX] = ELEMENT


Tuple
immutable, ()


Dictionary
Another type of list, stores data/values inside the curly brackets, {}.
Similart to a list, it mutable, however the index is a key, which is linked to data/values.

Ex.
student = {}
student["name"] = "John"
student["age"] = 12
student["weight"] = "120lbs"
student["school"] = "Evergreen"
student["Python"] = True

print (student)
print (student["weight"])


Time
Handles time-related tasks

Formula

import time   # Import the time library


Useful Time functions
1. time.time()
    - Returns floating-point numbers in seconds passed since epoch
    (Jan. 1st 1970, 00:00 UTC)
    - Use it for Date arthematic (etc. duration)
  
2. time.sleep(NUMBER)
    - Suspends (delays) execution of the current thread for the given number of seconds
'''

import time

print (time.time())

for x in range(10):
  print (str(x) + " second has passed")
  time.sleep(1)



# Exercise 1
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
'''
for x in range(5):  # [0, 1, 2, 3, 4]
  print ("*  " * (x + 1))
print ("\n\n")
# Exercise 2
'''
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
'''
for y in range(5):  # [0, 1, 2, 3, 4]
  print ("*  " * (5 - y))
print ("\n\n")
# Exercise 3
'''
            *
         *  *
      *  *  *
   *  *  *  *
*  *  *  *  *
'''
for i in range(5):
  print (" " * 3 * (4 - i) + "*  " * (i + 1))

print ("\n\n")
# Exercise 4
'''
*  *  *  *  *
   *  *  *  *
      *  *  *
         *  *
            *
'''
for j in range(5):
  print("   " * (j) + "*  " * (5 - j))
