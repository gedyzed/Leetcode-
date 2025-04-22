# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def bfs(node):

            if not node:
                return True 
            
            if self.value != node.val:
                return False

            queue = deque([node])
            visited = set([node])

            while queue:
                queue.popleft()

                if node.left not in visited:
                    visited.add(node.left)
                    if not bfs(node.left):
                        return False

                if node.right not in visited:
                    visited.add(node.right)
                    if not bfs(node.right):
                        return False

            return True            

        self.value = root.val
        if not bfs(root):
            return False

        return True



        