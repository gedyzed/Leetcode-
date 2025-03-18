# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        level_vals = defaultdict(list)
        def bfs(root, level):

            if not root:
                return 

            level_vals[level].append(root)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)    

        bfs(root, 0)  
        result, vals = [],list(level_vals.values())
        
        for i, val in enumerate(vals):
            if i % 2:
                left, right = 0, len(val) - 1  
                while left < right:
                    val[left].val, val[right].val = val[right].val, val[left].val

                    left += 1
                    right -= 1
               
        return vals[0][0]   
       