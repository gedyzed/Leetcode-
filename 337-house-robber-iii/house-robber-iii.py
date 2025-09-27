# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = defaultdict(int)
        def dp(node):

            if node in memo:
                return memo[node]
            
            if not node:
                return 0
            
            rob_it = node.val
            if node.left:
                rob_it += dp(node.left.left) + dp(node.left.right)
            if node.right:
                rob_it += dp(node.right.left) + dp(node.right.right)
            
            not_rob_it = dp(node.left) + dp(node.right)
            memo[node] = max(not_rob_it, rob_it)
            return memo[node]
            
        return dp(root)
       


        
        

        



        