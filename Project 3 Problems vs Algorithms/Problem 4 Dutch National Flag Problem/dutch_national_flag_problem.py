def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left,runner,right = 0, 0, len(input_list)-1
    while runner <= right:
        if input_list[runner] == 0:
            swap(input_list,left,runner)
            left += 1
        elif input_list[runner] == 2:
            swap(input_list,runner,right)
            right -= 1
            runner -= 1
        runner += 1 
    return input_list
        

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2,1, 1, 2, 0, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 2,  1, 1, 1, 2, 2, 2])