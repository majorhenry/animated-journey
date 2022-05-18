Problem 1: Square Root of an Integer
In the solution to this problem set, I solved it using Binary search and with every iteration, the algorithm trys to center the answer to the mid or approximately the mid-point of the interval between zero(start) and the given number(end). The method used to get the mid-point is much faster than just finding the floor division of the sum of the start and end points, since this is a binary search, the time complexity is O(logn) as half of the given interval is completely neglected with every intteration.

Efficiency

TIME COMPLEXITY
The time complexity is the same as that of a binary search algorithm which is; O(log N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)