# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, level):

            if not node:
                return 

            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = defaultdict(list)
        dfs(root, 0)
        return list(levels.values())    


                 






            


        