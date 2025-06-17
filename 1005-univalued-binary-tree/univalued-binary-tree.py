# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def bfs(root):
            queue = deque([root])
            visited = set()
            while queue:
                node = queue.popleft()
                if node:
                    if visited and node.val not in visited:
                        return False
                    visited.add(node.val)      
                    queue.append(node.left)
                    queue.append(node.right)  

            return True
        return bfs(root)    


            




        