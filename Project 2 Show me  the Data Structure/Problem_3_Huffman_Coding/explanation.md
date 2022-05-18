Problem 3: Huffman Coding
I solved this problem set by creating the freqency dictionary (freq_dict), that will store the characters in the passed data as keys and their number if occurrence as values, then this frequency dictionary is sorted based on the frequency, iterated and, the tree variable which is the huffman tree stores the character again as key and the value this time is the huffman code for each charater in the freq_dict. Now I went ahead and encode the whole message by creating a string variable encoded_msg which for every character in the data, it appends the huffman code for it in the encoded_msg, and creates a code string for the input data, the encoded_msg and the tree are returned by the huffman_encoding method. These returned values are all the huffman_decoding method needs to decode the message, in the decoding method firstly I created the swap_dict variable which allows me to swap the key:value pair of the tree variable to value:key and this will enable me to search the tree dict with it's key which is not easily possible for dictionaries in general and now using ones as a break point in the string of data,  after every '1' I used it as key to seach for the corresponding value in the swap_dict and append it to the decoded_msg string variable, and finally after the iteration, the method returns the decoded_msg.

Efficiency

TIME COMPLEXITY
The time complexity of the encoding method is linearly dependent on the input string, even though I used the sorted method which uses Timsort with a complexity of nlogn, but in general we have; O(N)
The decoding method also takes linear time complexity to decode the data even though searching the dictionary is constant time but we have to itrate through the whole data first; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent on the input string as the code has to iterate through every char; O(N)