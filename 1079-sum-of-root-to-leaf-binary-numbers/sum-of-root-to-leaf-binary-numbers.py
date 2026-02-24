# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        queue = deque([(root, root.val)])
        sum = 0
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                sum += val

            if node.left:
                new_val = (val << 1) | node.left.val
                queue.append((node.left, new_val))
            
            if node.right:
                new_val = (val << 1) | node.right.val
                queue.append((node.right, new_val))
            
        return sum

               