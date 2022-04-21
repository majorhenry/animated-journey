import sys

def huffman_encoding(data):
    freq_dict = {}
    tree = {}
    code = '1'
    encoded_msg = ''
    
    for letter in data:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1
    
    for item in sorted(freq_dict.items(), key=lambda x:x[1]):
        tree[item[0]] = code
        code = '0' + code
    
    for letter in data:
        encoded_msg += tree[letter]
        
    return encoded_msg, tree
    
def huffman_decoding(data, tree):
    swap_dict = {}
    decoded_msg_helper, decoded_msg = '',''
    
    
    swap_dict = {value:key for key, value in tree.items ()}
    
    for char in data:
        if char == '1':
            decoded_msg_helper += char
            decoded_msg += swap_dict[decoded_msg_helper]
            decoded_msg_helper = ''
        else:
            decoded_msg_helper += char
            
    return decoded_msg




if __name__ == "__main__":

    #Test Case 1
    print("Test Case 1")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print()
    print()

    #Test Case 2
    print("Test Case 2")

    a_great_sentence = "aaaaaaaaaaaaaa"     #An edge case with same char in a string

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print()
    print()

    #Test Case 3
    print("Test Case 3")
    a_great_sentence = " "     #An edge case of empty string

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print()
    print()

    #Test Case 4
    print("Test Case 4")
    a_great_sentence = "a"     #An edge case with a char

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


