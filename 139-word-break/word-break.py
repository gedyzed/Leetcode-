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
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.is_end
   
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        word_dicts = set(wordDict)
        memo = [False] * (len(s) + 1)
        memo[-1] = True
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s) + 1):
                if trie.search(s[start:end]) and memo[end]:
                    memo[start] = True
                    break
        
        return memo[0]








                




            
           

            

