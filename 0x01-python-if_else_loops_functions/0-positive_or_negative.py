#!/usr/bin/python3
import random
number = random.int(-10, 10)
if number > 0:
    print(f"{number} is posiive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
