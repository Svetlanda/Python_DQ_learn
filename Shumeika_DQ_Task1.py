# HOME TASK 1
# Create a python script:
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.

import random

# declaration of variables

r = range(0, 100)
a = 0  # random start value
b = 1000  # random end value
randomlist = []

# creation of random value list

for i in r:
    n = random.randint(a, b)
    randomlist.append(n)
print("Original list: ", randomlist)

# sorting the list in ascending order

for i in range(0, len(randomlist)):
    for j in range(i + 1, len(randomlist)):
        if randomlist[i] >= randomlist[j]:
            randomlist[i], randomlist[j] = randomlist[j], randomlist[i]
print("Sorted list: ", randomlist)

# calculation of even numbers average

even_count, odd_count, even_sum, odd_sum = 0, 0, 0, 0 #variable declaration

for i in range(0, len(randomlist)):
    if randomlist[i] % 2 == 0:
        even_count += 1
        even_sum += randomlist[i]
    else:
        odd_count += 1
        odd_sum += randomlist[i]
#print("even_count = ", even_count)
#print("even_sum = ", even_sum)
#print("odd_count = ", odd_count)
#print("odd_sum = ", odd_sum)

try:
    print("Odd avg = ", odd_sum / odd_count)
except ZeroDivisionError:
    print("Odd Error division by 0")
# here is 2 block just in case one of them catch error.
try:
    print("Even avg = ", even_sum / even_count)
except ZeroDivisionError:
    print("Even Error division by 0")
