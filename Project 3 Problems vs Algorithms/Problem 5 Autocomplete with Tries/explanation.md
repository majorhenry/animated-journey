Problem 5: Autocomplete with Tries
In the solution to this problem set, I solved it using dictionary for the trie node children and boolean for the is_word attribute.

Efficiency

TrieNode:
insert():
TIME COMPLEXITY
The time complexity is linearly dependent to the number of characters that needs to be inserted; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent to the number of characters in the word to be inserted as each character is assigned a node; O(N)

Trie:
find():
TIME COMPLEXITY
The time complexity is the linearly dependent to the lenght of characters in the word if the word exists in the trie; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)

insert():
TIME COMPLEXITY
The time complexity is linearly dependent as the code has to iterate through the characters of the word to be inserted; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent to the number of characters in the word to be inserted; O(N)

TrieNode:
insert():
TIME COMPLEXITY
The time complexity is linearly dependent to the number of characters that needs to be inserted; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent to the number of characters in the word to be inserted as each character is assigned a node; O(N)

suffixes():
TIME COMPLEXITY
The time complexity is linearly dependent to words starting with similar characters; O(N)

SPACE COMPLEXITY
The space complexity is constant space as no extra memory is used; O(1)


 