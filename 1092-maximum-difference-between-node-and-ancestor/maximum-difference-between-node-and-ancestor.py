# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.diff = 0
        def maxRange(root, max_, min_):

            if not root:
                return 

            max_ = max(root.val, max_)
            min_ = min(root.val, min_)
            self.diff = max(self.diff, max_ - root.val, root.val - min_)

            maxRange(root.left, max_, min_)
            maxRange(root.right, max_, min_)

        maxRange(root, 0, 5001)  
        return self.diff  


        