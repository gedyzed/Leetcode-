from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat):

        direction = False
        forward_dgl = defaultdict(list)
        backward_dgl = defaultdict(list)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                    
                if not direction:
                    forward_dgl[row + col].append(mat[row][col])
                else:
                    backward_dgl[row + col].append(mat[row][col]) 
                    
                direction = not direction

            if len(mat[0]) % 2 == 0:
                direction = not direction       


        result = []     
        backward_dgl = list(backward_dgl.values())  
        forward_dgl = list(forward_dgl.values())  

        print(forward_dgl,   backward_dgl)

        direction = False
        left = right = 0
        while left < len(backward_dgl) and right < len(forward_dgl):
            if not direction:
                forward_dgl[right].reverse()
                result.extend(forward_dgl[right])
                direction = not direction
                right += 1
            else:
                result.extend(backward_dgl[left])
                direction = not direction
                left += 1
                

        if not direction:
            while right < len(forward_dgl):
                forward_dgl[right].reverse()
                result.extend(forward_dgl[right])
                right += 1
        else:
            while left < len(backward_dgl):
                result.extend(backward_dgl[left])
                left += 1

        return result   
        