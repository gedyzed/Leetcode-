class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:

        result = []
        
        left, right = 0, len(mat[0]) 
        top, bottom = 0, len(mat)
        
        while left < right and top < bottom:
            
            for i in range(left, right):
                result.append(mat[top][i])
            top += 1
                
            for i in range(top, bottom):
                result.append(mat[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                result.append(mat[bottom -1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1 ):
                result.append(mat[i][left])
            left += 1
        
        return result 
                        

        

  




  