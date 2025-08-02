# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def helper(root, path, pathsum):

            if not root:
                return

            pathsum += root.val
            path.append(root.val)
            if pathsum == targetSum and not root.right and not root.left:
                res.append(path[:])

            helper(root.left, path, pathsum)
            helper(root.right, path, pathsum)  

            path.pop()

        res = []
        helper(root, [], 0)
        return res    

