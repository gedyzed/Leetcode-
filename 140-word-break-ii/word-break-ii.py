class TrieNode:
    def __init__(self):
        self.is_word = False
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
        cur.is_word = True
        
    def search(self, idx, dp, s):
        cur = self.root
        for j in range(idx, len(s)):
            c = s[j]
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if cur.is_word:
                dp[j] = True
    
    def searchWord(self, word) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                trie.search(i, dp, s)
            
        if not dp[-1]:
            return []
        
        def backtrack(idx):
            
            if idx == len(s):
                ans.append(" ".join(words))
                return 
            
            for i in range(idx + 1, len(s) + 1):
                cur_word = s[idx: i]
                if trie.searchWord(cur_word):
                    words.append(cur_word)
                    backtrack(i)
                    words.pop()
               
        words, ans = [], [] 
        backtrack(0)
        return ans

        