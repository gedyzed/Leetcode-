
class Solution:
    def findDiagonalOrder(self, mat):

        direction = False
        forward_dgl, backward_dgl = defaultdict(list), defaultdict(list)

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
        b_dgl, f_dgl  = list(backward_dgl.values()), list(forward_dgl.values())   
        left = right = 0
        
        range_ = max(len(f_dgl), len(b_dgl))
        for i in range(range_): 
            result.extend(reversed(f_dgl[i]))
            if i < len(b_dgl):
                result.extend(b_dgl[i])
    
        return result   
        