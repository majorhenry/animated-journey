from math import inf

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if type(ints) != list:
        print("INVALID INPUT")
        return
    min, max = inf, 0

    for i in ints:
        if i < min:
            min = i

        if i > max:
            max = i
    print(min,max)
    return min,max


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

nums = [i for i in range(0, 1090)]  # a list containing 0 - 1089
random.shuffle(nums)
print ("Pass" if ((0, 1089) == get_min_max(nums)) else "Fail")

nums = [i for i in range(47, 109)]  # a list containing 47 - 108
random.shuffle(nums)
print ("Pass" if ((47, 108) == get_min_max(nums)) else "Fail")

nums = [i for i in range(0)]  # a list containing  nothing
random.shuffle(nums)
print ("Pass" if ((inf,0) == get_min_max(nums)) else "Fail")

nums = [i for i in range(0, 1)]  # a list containing  zeros
random.shuffle(nums)
print ("Pass" if ((0,0) == get_min_max(nums)) else "Fail")

# Sorting usually requires O(n log n) time Can you 
# come up with a O(n) algorithm 
# (i.e., linear time)?