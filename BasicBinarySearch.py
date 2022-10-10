# Basic implementation of binary search algorithim

# Help visualize the optimization and how its faster than a basic search

# aka going through the whole list and checking values
import random
import time

def BasicSearch(l, target):
    # example list = [1, 4, 8, 10]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search or dictionary search as i like to call it, divides the work !
# also optimize search by sorting a list when possible
def BinarySearch(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1 # target not in list

    # use same example list as above
    midpoint = ((low + high) // 2)

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return BinarySearch(l, target, low, midpoint-1)
    else:
        # checking whats to the right of the targer
        return BinarySearch(l, target, midpoint+1, high)

dataset = list(range(1,100000001))
#print(dataset)

BasicStart = time.process_time()
BasicSearch(dataset, 999999)
BasicEnd = time.process_time() - BasicStart
print(f"Basic search time was: {BasicEnd}")

BinaryStart = time.process_time()
BinarySearch(dataset, 999999)
BinaryEnd = time.process_time() - BinaryStart
print(f"Basic search time was: {BinaryEnd}")