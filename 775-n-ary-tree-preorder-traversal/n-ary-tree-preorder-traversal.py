"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:

        def preOrder(root):

            if not root:
                return []

            result= [root.val]
            for child in root.children:
                result.extend(preOrder(child))
                
            return result  

        return preOrder(root)      





        