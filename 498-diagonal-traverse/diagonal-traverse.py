class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:


        m, n = len(mat), len(mat[0]) 
        r = c = 0
        res = [0] * (m * n) 
        for i in range(m * n):
            res[i] = mat[r][c]
            if (r + c) & 1:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
            else:
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1  
                else:
                    r -= 1
                    c += 1
               
        return  res                  
        

    



        