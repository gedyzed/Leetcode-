# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        result = []
        def evenSum(node, parent, gp):

            if not node:
                return 

            if gp and not (gp.val % 2):
                result.append(node.val)   

            evenSum(node.left, node, parent)    
            evenSum(node.right, node, parent)

        evenSum(root, None, None)
        return sum(result)      