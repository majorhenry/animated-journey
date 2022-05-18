def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start,end = 0, len(input_list) - 1

    while start <= end:
        mid = (start + end)//2
        if number == input_list[mid]:
            return mid
        #check if mid belongs to the the left sorted portion
        if input_list[start] < input_list[mid]:
            #conditions that can cause tthe left most pointer to move forward
            if number > input_list[mid] or number < input_list[start]:
                start = mid + 1
            #else move the right pointer backwards
            else: 
                end = mid - 1
        #Hence the mid belongs to the right sorted array members
        else:
            #conditions that can cause the right most pointer to be moved backwards
            if number > input_list[end] or number < input_list[mid]:
                end = mid - 1
            #else move the left most pointer forward
            else:
                start = mid + 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4,5,6,7,0,1,2], 0]) #, Output: 4
test_function([[1,3,5,7,9,11.13,16],11]) # Testing a sorted array