# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        def paths(root, res):

            if not root:
                return 
   
            r = copy.deepcopy(res)
            r.append(f"{root.val}")
            if not root.left and not root.right:
                result.append("->".join(r))
                return 

            paths(root.left, r)
            paths(root.right, r)
                     
        paths(root, [])
        return result      







        
        