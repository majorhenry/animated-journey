class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    def find(self, prefix):
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return current




# In[13]:


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
   
    def suffixes(self, suffix = ''):
        for key, value in self.children.items():
            if value.is_word:
                suffixes.append(suffix + key)
            if value.children:
                suffixes += value.suffixes(suffix + key)
        return suffixes 
        
    def __repr__(self):
        return f"{self.is_word}" #children.values()


# # Testing it all out


# In[21]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


    
### find
print("Pass" if type(MyTrie.find("t")) is TrieNode else "Fail") 
print("Pass" if MyTrie.find("q") is not False else "Fail") #returns false because d doesn't exist in the Trie
print(MyTrie.find('ants')) #returns false because 'ants' is not a word in wordList
print(MyTrie.find('')) #Empty string edge case

assert type(MyTrie.find('a')) is TrieNode
assert MyTrie.find('function').is_word is True

### Suffixes
node = MyTrie.find('an')
assert node.suffixes() == ['t', 'thology', 'tagonist', 'tonym']

node = MyTrie.find('anta')
assert node.suffixes() == ['gonist']

node = MyTrie.find('')
assert node.suffixes() == ["ant", "anthology", "antagonist", "antonym", "fun", "function", "factory", "trie", "trigger", "trigonometry", "tripod"]

