## Time
Handles time-related tasks

### Formula
```python
# Import the time library
import time		# Top of the page
```

### Useful functions
1. time.time()
- Returns floating-point numbers in seconds passed since epoch (Jan. 1st, 1970, 00:00 at UTC)
- Use it for Date arithmetics (etc. duration)
```python
import time

# Function: time() 
seconds = time.time()
print ("Seconds since epoch = " + str(seconds))
```
> 1614308795.447049

2. time.sleep()
- Suspends (delays) execution of the current thread for the given number of seconds
```python
import time

# Function: sleep()
print(1)
time.sleep(4) # Pausing the program for 4 seconds
print(5)
```
> 1
> 5