# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        level_vals = defaultdict(list)
        def bfs(root, level):

            if not root:
                return 

            level_vals[level].append(root.val)

            bfs(root.left, level + 1)
            bfs(root.right, level + 1)    

        bfs(root, 0)  
        result, i = [], 0
        for val in level_vals.values():
            if i % 2: 
                val.reverse()
                result.append(val) 
            else:
                result.append(val) 

            i += 1      


        return result
    