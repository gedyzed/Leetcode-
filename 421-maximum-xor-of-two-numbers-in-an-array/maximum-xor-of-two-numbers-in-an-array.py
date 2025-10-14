class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(2)]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if cur.children[bit] == None:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]

        cur.is_end = True
    
    def getMax(self, num):
        cur = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if cur.children[toggled]:
                xor = xor | (1 << i)
                cur = cur.children[toggled]
            else:
                cur = cur.children[bit]
        
        return xor
      
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        maxXOR = 0
        for num in nums:
            maxXOR = max(maxXOR, trie.getMax(num))
        return maxXOR
        