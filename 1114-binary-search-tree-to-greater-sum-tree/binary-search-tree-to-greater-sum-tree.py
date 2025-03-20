# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return 

            dfs(root.right)
            self.max += root.val
            root.val = self.max
            dfs(root.left) 

        self.max = 0    
        dfs(root)    
        return root     




        
        