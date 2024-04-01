class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)     #column
        n = len(matrix[0])  #row
        
        newMatrix = []
        column = [] 
        
        for i in range(n):
            for j in range(m):          
               column.append(matrix[j][i]) 
            newMatrix.append(column) 
            column = []  
            
        return newMatrix 
           
        
        
        