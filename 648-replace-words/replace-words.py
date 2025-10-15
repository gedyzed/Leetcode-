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
    
    def hasRoot(self, word) -> str:
        cur = self.root
        for i, c in enumerate(word):
            if cur.is_end:
                return word[:i]
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        words = sentence.split()
        for i in range(len(words)):
            word = trie.hasRoot(words[i])
            if word:
                words[i] = word

        return " ".join(words)

        