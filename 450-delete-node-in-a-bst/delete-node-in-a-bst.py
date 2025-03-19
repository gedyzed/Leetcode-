# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(node):

            while node.left:
                node = node.left
            return node

        def delete(root, key):

            if not root:
                return root

            if root.val > key:
                root.left = delete(root.left, key)  
            elif root.val < key:
                root.right = delete(root.right, key)      
            else:
                # case 1
                if not root.right and not root.left:
                    return None

                # case 2
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right

                #minimun node in the right sub-tree
                min_node = find_min(root.right)    
                root.val, min_node.val = min_node.val, root.val
                root.right = delete(root.right, min_node.val)

            return root 

        return delete(root, key)    







        