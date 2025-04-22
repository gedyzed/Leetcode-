# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels, level = [], 0
        queue = deque([(root, 0)])
        curr_level = []

        while queue:  
            node, node_level = queue.popleft()

            if not node:
                continue

            if node_level != level:
                levels.append(curr_level[:])
                level += 1
                curr_level = []

            curr_level.append(node.val)
            queue.append([node.left, level + 1])
            queue.append([node.right, level + 1]) 

        if curr_level:
            levels.append(curr_level[:])
            
        return levels            






            


        