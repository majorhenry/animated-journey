Problem 7: Request Routing in a Web Server with Tries
In the solution to this problem set, I solved it very similarly like the Problem 5 except that I added some methods as described the problem set, also I had to format the string of the path variable and convert it to an array from which each word in the string is added as node instead of each character like in Problem 5

Efficiency

Add Handler:
TIME COMPLEXITY
The time complexity is linearly dependent to the number of words in path; O(N)

SPACE COMPLEXITY
The space complexity is also linearly dependent to the number of words as a TrieNode is created for every word in path


lookup:
TIME COMPLEXITY
The time Complexity is linearly dependent to the lenght of the trie as lookup method have to traverse the whole lenght to look for it; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)
