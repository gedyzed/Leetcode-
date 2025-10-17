class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
  
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        root = TrieNode()
        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_word = True
        
        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                cur = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in cur.children:
                        break
                    cur = cur.children[c]
                    if cur.is_word:
                        dp[j] = True
        
        return dp[-1]

