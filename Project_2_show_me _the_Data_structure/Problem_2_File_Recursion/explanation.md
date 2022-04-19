Problem 2: File Recursion
The solution to this problem set is firstly I searched for all files with the suffix in the path and if the file existes there, it's being added to the files list data type and now I further went to add all the folders to the folders list and recursively searched for the suffix again in the sub folders and if found, it's being added to the files list and finally returned. 


Efficiency

TIME COMPLEXITY
The time complexity is linearly dependent on the number of directories to be searched before finding the file; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent on the number of returned files; O(N)