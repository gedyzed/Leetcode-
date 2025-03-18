# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def pathSum(root, sum):

            if not root:
                return root

            sum = sum * 10 + root.val
            if not root.left and not root.right:
                self.total += sum

            pathSum(root.left, sum)  
            pathSum(root.right, sum)  

        pathSum(root, 0)    
        return self.total

        