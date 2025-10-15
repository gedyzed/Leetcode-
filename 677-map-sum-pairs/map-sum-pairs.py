class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
    
    def prefix(self, pre):
        cur = self.root
        for c in pre:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        words = [] 
        def collect(root, word):
            if not root:
                return 
            
            if root.is_end:
                words.append(word)
            
            for c in root.children:
                cur = root.children[c]
                collect(cur, word + c)
        
        collect(cur, pre)
        return words

             
class MapSum:

    def __init__(self):
        self.map_sum = {}
        self.trie = Trie()
    
    def insert(self, key: str, val: int) -> None:
        self.map_sum[key] = val
        self.trie.insert(key)

    def sum(self, prefix: str) -> int:
        words = self.trie.prefix(prefix)
        sum = 0
        for word in words:
            sum += self.map_sum[word]

        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)