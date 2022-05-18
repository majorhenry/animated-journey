import time

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start, end = 0, number + 1
    while start < end:
        mid = start + (end - start)//2
        if mid*mid == number :
            return mid
        elif (end - start) == 1:
            return start
        elif mid*mid > number:
            end = mid 
        else:
            start = mid

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")