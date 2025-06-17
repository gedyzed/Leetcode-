# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root):
            
            if not root:
                return []

            res = defaultdict(list)
            queue = deque([(root, 0)])
            while queue: 
                node, lvl  = queue.popleft() 
                res[lvl].append(node.val)
                if node.left:
                    queue.append((node.left, lvl + 1)) 
                if node.right:
                    queue.append((node.right, lvl + 1))  
                
            return list(res.values())
        return bfs(root)    

                





   


                 






            


        