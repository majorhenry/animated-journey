Problem 6: Union and Intersection
The problem set is solved by iterating through the linked list and using a set data type(temp_set) to store the values of the linked list, this automatically takes care of repetitive values for the union method, and for the intersection method, while iterating one of the linked list, each value is being searched for in the other linked list and if it exists, the value gets stored n the temp_set variable else move to the next value. Finally the values in the temp_set variable are added to a newly created linked list then returned and if the linked list is empty the method returns None. 

 Efficiency

TIME COMPLEXITY
The time complexity of the union method is linearly dependent on the size of the iterated linked lists; O(N).
The time complexity of the intersection method is also linearly dependent on the size of the iterated linked list; O(N).
The time complexity of appending item the newly created linked list also has a linear time complexity; O(N).
The total time complexity is quadratic; O(N²)

SPACE COMPLEXITY
The space complexity depends linearly to the size of the linked lists being iterated; O(N) 