# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def path(root, pathsum, nums_str):

            if not root:
                return

            pathsum += root.val
            nums_str += str(root.val) + ","
            
            if pathsum == targetSum and not root.right and not root.left:
                res.append(nums_str)
                return 

            path(root.left, pathsum, nums_str)
            path(root.right, pathsum, nums_str)    

         
        res = [] 
        path(root, 0, "")
        ans = []
        for r in res:
            r = r.split(",")
            r = [int(num) for num in r if num != ""]
            ans.append(r)

        return ans    


                
         
        