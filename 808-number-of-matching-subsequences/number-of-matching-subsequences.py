class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_count = 0  

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
   
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end_count += 1  

        waiting = defaultdict(list)
        for c, node in root.children.items():
            waiting[c].append(node)

        count = 0
        for c in s:
            current = waiting[c]
            waiting[c] = []

            for node in current:
                if node.end_count > 0:
                    count += node.end_count  

                for nxt, nxt_node in node.children.items():
                    waiting[nxt].append(nxt_node)

        return count
