# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def getNodes(root):

            if not root:
                return root

            nodes.append(root.val)
            getNodes(root.right)
            getNodes(root.left)

        def buildBST(left, right):

            if left > right:
                return 

            mid = (left + right) // 2
            root = TreeNode(nodes[mid]) 
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)

            return root
            
        nodes = []
        getNodes(root)
        nodes = sorted(nodes)  
        return buildBST(0, len(nodes) - 1)

        
   

        

        