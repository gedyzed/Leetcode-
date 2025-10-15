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

    def suggestion(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        def collect(root, word):
            if not root:
                return 
            
            if root.is_end:
                words.append(word)
            
            for c in root.children:
                cur = root.children[c]
                collect(cur, word + c)

        words, word = [], prefix
        collect(cur, prefix)
        return sorted(words)[:3] if len(words) > 3 else sorted(words)   

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie()
        for product in products:
            trie.insert(product)
        
        ans = []
        prefix = searchWord[0]
        for i in range(1, len(searchWord)):
            ans.append(trie.suggestion(prefix))
            prefix += searchWord[i]
        ans.append(trie.suggestion(prefix))

        return ans 
     