Problem 1: LRU Cache
In this problem set I implemented the solution using an orderedDict as it helps me to keep record of order of inputs, or sets. Further more the get method of the ordered dict can also take a default value which is returned in the absence of a given value in the orderedDict. Lastly the popitem method of the orderedDict takes parameter of whether to start deleting from the beginning(last = False) or last item (last = True), so in my implementation, if there is a cache hit in the self.store, it is also being deleted and reinserted in the cache so the orderedDict automatically keeps recored of the least recently used cache.

Efficiency

TIME COMPLEXITY
The time complexity of the set method of the LRU_Cache is constant time; O(1) 
The time complexity of the get method of the LRU_Cache is also constant time, because looking up in a dictionary is constant time; O(1)

SPACE COMPLEXITY
The space complexity is linearly dependent on the capacity of the LRU cache; O(N)