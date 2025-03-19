# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

            if not root1 and not root2:
                return None

            if not root1 and root2:
                root = TreeNode(root2.val)
                root.left = self.mergeTrees(root1, root2.left)
                root.right = self.mergeTrees(root1, root2.right)
                return root

            if root1 and  not root2:
                root = TreeNode(root1.val)
                root.left = self.mergeTrees(root1.left, root2)
                root.right = self.mergeTrees(root1.right, root2)  
                return root

            root = TreeNode(root1.val + root2.val)      
            root.left = self.mergeTrees(root1.left, root2.left)   
            root.right = self.mergeTrees(root1.right, root2.right)

            return root

                    
                
