# Exercise: 02 Good Morning Ma'am
# Question: Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

# With the help of the hint provided, we can use the time module in Python to get the current time and its components.
# Here's how you can do it:

import time

current_time = time.strftime("%H:%M:%S")
print("Current Time =", current_time)

current_hour = time.strftime("%H")
print("Current Hour =", current_hour)

current_minute = time.strftime("%M")
print("Current Minute =", current_minute)

current_second = time.strftime("%S")
print("Current Second =", current_second)

# This code will print the current time in hours, minutes, and seconds, in the form of strings.
# But, we can't perform any mathematical operations on these string values.
# To convert them into integers, we can use the int() function as follows:

current_hour = int(time.strftime("%H"))
print("Current Hour (as integer) =", current_hour)

if current_hour > 0 and current_hour < 12:
    print("Good Morning, Ma'am!")
elif current_hour >= 12 and current_hour < 17:
    print("Good Afternoon, Ma'am!")
elif current_hour >= 17 and current_hour < 21:
    print("Good Evening, Ma'am!")
else:    
    print("Good Night, Ma'am!")