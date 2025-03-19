"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        level_vals = defaultdict(list)
        def dfs(root, level):

            if not root:
                return 

            level_vals[level].append(root.val)   
            for child in root.children:
                dfs(child, level + 1)

        dfs(root, 0)    
        return level_vals.values()     
        