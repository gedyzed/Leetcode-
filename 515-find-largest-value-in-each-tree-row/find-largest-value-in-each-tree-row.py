# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        def maxValue(root, depth):

            if not root:
                return 

            if depth == len(result):
                result.append(root.val)    
            else:
                result[depth] = max(result[depth], root.val) 

            maxValue(root.left, depth + 1)     
            maxValue(root.right, depth + 1)
     
        maxValue(root, 0)
        return result       



        