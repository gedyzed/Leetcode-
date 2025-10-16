class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
    
    def search(self, word) -> bool:  
        def helper(cur, idx, word):
            for i in range(idx + 1, len(word)):
                c = word[i]
                if c == ".":
                    for ch in cur.children:
                        if helper(cur.children[ch], i, word):
                            return True

                    return False
                else:
                    if c not in cur.children:
                        return False 
                    cur = cur.children[c]
                
            return cur.is_end 

        cur = self.root
        return helper(cur, -1, word)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        
    def search(self, word: str) -> bool:
        return self.trie.search(word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)