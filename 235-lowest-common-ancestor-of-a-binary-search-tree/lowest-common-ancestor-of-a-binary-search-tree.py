# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root):

            if not root:
                return 

            if min(p.val, q.val) <= root.val <= max(p.val, q.val):
                root.val
                return root
                
            return lca(root.left) or lca(root.right) 

        return lca(root)        


        