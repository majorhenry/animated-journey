"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria
 
 to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the 
least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used 

entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

"""

from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
       
       res = self.store.get(key, -1)
       if res == -1:
            return res
       else:
            ret = self.store.pop(key)
            self.store[key] = ret
            return res

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        self.store[key] = value

        if len(self.store) > self.capacity:
            self.store.popitem(last = False)
            


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(4))      # returns 4 

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(our_cache.get(5))
print(our_cache.get(6))


another_cache = LRU_Cache(8)

another_cache.set(1, 1);
another_cache.set(2, 2);
another_cache.set(3, 3);
another_cache.set(4, 4);


print(another_cache.get(1))     # returns 1
print(another_cache.get(2))       # returns 2
print(another_cache.get(9))      # returns -1 because 9 is not present in the cache
print(another_cache.get(4))      # returns 4 

another_cache.set(5, 5) 
another_cache.set(6, 6)

print(another_cache.get(3))     ## returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(another_cache.get(5))
print(another_cache.get(6))

another_cache.set(7, 1234)
another_cache.set(8, 123)
another_cache.set(6, 101)  
another_cache.set(3, 900)
another_cache.set(9,999)    # least recently used deleted
another_cache.set(10,1010)  # least recently used deleted

print()
print(another_cache.get(7))
print(another_cache.get(8))

print()
print(another_cache.get(6))
print(another_cache.get(3))
print(another_cache.get(9))
print(another_cache.get(6))

print()
print(another_cache.get(1))     #returns -1
print(another_cache.get(2))     # returns -1