Problem 7: Request Routing in a Web Server with Tries
In the solution to this problem set, I solved it very similarly like the Problem 5 except that I added some methods as described the problem set, also I had to format the string of the path variable and convert it to an array from which each word in the string is added as node instead of each character like in Problem 5

Efficiency

RouteTrie:
insert():
TIME COMPLEXITY
The time complexity is linearly dependent as the code has to iterate through paths; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent to the number of path in paths that will be inserted; O(N)

find():
TIME COMPLEXITY
The time complexity is the linearly dependent to the number of path in the paths array; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)

RouteTrieNode:
insert():
TIME COMPLEXITY
The time complexity is constant time as it just assigns a RouteTrieNode to a given path; O(1)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)

Router:
Add Handler():
TIME COMPLEXITY
The time complexity is linearly dependent to the number of words in path; O(N)

SPACE COMPLEXITY
The space complexity is also linearly dependent to the number of words as a TrieNode is created for every word in path

lookup():
TIME COMPLEXITY
The time Complexity is linearly dependent to the lenght of the trie as lookup method have to traverse the whole lenght to look for it; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)

split_path():
TIME COMPLEXITY
The replace method uses a linear time complexity; O(N)
The split method uses a linear time complexity; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)