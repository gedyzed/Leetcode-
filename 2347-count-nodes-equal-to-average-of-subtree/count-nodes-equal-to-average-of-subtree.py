# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def average(root):
            if not root:
                return 0, 0

            n, sum1 = average(root.left)  
            m, sum2 = average(root.right) 
            
            n =  n + m + 1
            sum1 = sum1 + sum2 + root.val
            avg = sum1 // n 
            
            if root.val == avg:
                self.count += 1

            return n, sum1

        self.count = 0  
        average(root)  
        return self.count








        