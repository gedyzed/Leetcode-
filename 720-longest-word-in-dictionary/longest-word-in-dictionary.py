class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, max_word):
        cur, status = self.root, True
        for i, c in enumerate(word):  
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  
            if i < len(word) - 1:
                status = status and cur.is_end

        cur.is_end = True
        if status and len(max_word) < len(word):
            return word
        return max_word

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        words.sort()
        ans = ""
        for word in words:
            ans = trie.insert(word, ans)
        
        return ans
            

        