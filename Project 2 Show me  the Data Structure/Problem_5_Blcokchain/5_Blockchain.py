import hashlib
from time import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = f"Time stamp: {self.timestamp}, Data: {self.data}, Previous hash: {self.previous_hash}".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.head = None
        self.last_node = None
        self.next = None
        self.prev = None

    def add_block(self, data):
        if self.head is None:
            self.head = Block(timestamp=time(), data=data, previous_hash=None)
            self.last_node = self.head
            return

        self.last_node.next = Block(timestamp=time(), data=data, previous_hash=self.last_node.hash)
        self.last_node.next.prev = self.last_node
        self.last_node = self.last_node.next
        return

    def __iter__(self):
        node = self.last_node
        while node.previous_hash:
            yield node.hash
            node = node.prev
        else:
            yield self.head.hash

    def __repr__(self):
        blocklist = []
        for block in self:
            blocklist.append(block)

        #reversed so we start with the lastly added block to the chain
        blocklist.reverse()
        return str(blocklist)

#First Test Case
blockchain_1 = BlockChain()
blockchain_1.add_block("First")
print(blockchain_1)
print()

blockchain_1.add_block("Second")
print(blockchain_1)
print()

#Second Test Case
blockchain_2 = BlockChain()

list_test = ["First set of sample test string", "should be stright forward compared to the second sample of string",
             "as this will add the number of elements in this list,", "to the block chain as a block sequentially"]

for item in list_test:
    blockchain_2.add_block(item)

print(blockchain_2)
print()

#Third Test Case
blockchain_3 = BlockChain()

lyrics = ["I Could See The Whole City From This Balcony","Back In 2019, I Was Outside Freely","But Now They Got It Out For Me",
            "I Don't Care What Frat That You Was In","You Can't Alpha Me, Keep Dreaming"]

for line in lyrics:
    blockchain_3.add_block(line)

print(blockchain_3)
