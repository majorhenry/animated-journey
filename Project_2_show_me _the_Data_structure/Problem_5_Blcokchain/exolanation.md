Problem 5: Blockchain
In the solution to this problem set, I solved it by creating a singly-linked list (BlockChain) with evry node equals to instance of the Block class. New nodes/blocks are appended to the linked list and the time module is used to keep recored of time of creation of each block.

Efficiency

TIME COMPLEXITY
The time complexity is adding new block is constant time because I kept record of the last node; O(1)
The iter dunder method has a linear time complexity; O(N)

SPACE COMPLEXITY
The space complexity is linearly dependent number of nodes being added;O(N)