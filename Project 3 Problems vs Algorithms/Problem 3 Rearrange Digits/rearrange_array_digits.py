def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """ 
    if len(input_list) == 0 or type(input_list) != list:
        print("INVALID INPUT")
        return
    
    def mergeSort(myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive calling each half
            mergeSort(left)
            mergeSort(right)

            # Two pointers for iterating the two halves
            i = 0
            j = 0
            
            # pointer for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1

    
    mergeSort(input_list)
    string1,string2 = '',''

    
    swt = True
    for i in range(len(input_list)-1,-1,-1):
        if swt:
            string1 += str(input_list[i])
            swt = False
        else:
            string2 += str(input_list[i])
            swt = True 
    return [int(string1),int(string2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    if type(output) != list:
        return
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4,6,2,5,9,8], [964, 852]])
test_function([[], [964, 852]])     #INVALID INPUT
test_function(["Hi mom", [964, 852]])   #INVALID INPUT
