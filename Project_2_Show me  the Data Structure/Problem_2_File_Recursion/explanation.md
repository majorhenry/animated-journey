Problem 2: File Recursion
The solution to this problem set is firstly I searched for all files with the suffix in the path and if the file existes there, it's being added to the files list data type and now I further went to add all the folders to the folders list and recursively searched for the suffix again in the sub folders and if found, it's being added to the files list and finally returned. 


Efficiency

TIME COMPLEXITY
Time Complexity is O(n*l) as in the worst-case scenario, if each entry is a subfolder, the function will be called n times and we have to check if the filename ends with the suffix which is of time complexity O(l) where l is the length of the suffix; O(N).

SPACE COMPLEXITY
Space Complexity is O(m * n) where m is the maximum depth of the list and n is the number of times the function is called; O(N).