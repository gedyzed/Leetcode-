# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        result = []
        def pathSum(root, sum, tg):

            if not root:
                return False

            sum += root.val
            if sum == tg and not root.right and not root.left:
                return True

            return pathSum(root.right, sum, tg) or pathSum(root.left, sum, tg)

        return pathSum(root, 0, targetSum)   


        