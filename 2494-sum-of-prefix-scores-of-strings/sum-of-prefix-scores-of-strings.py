class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                cur.count[c] = 0
            cur.count[c] += 1
            cur = cur.children[c]
        cur.is_end = True
    
    def prefixSum(self, pre) -> int:
        cur, sum = self.root, 0
        for c in pre:
            if c not in cur.children:
                return sum
            
            sum += cur.count[c]
            cur = cur.children[c]

        return sum

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        for word in words:
            ans.append(trie.prefixSum(word))
        
        return ans


        
        