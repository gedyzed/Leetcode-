class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        def pascal_triangle(rows):    
            if not rows:
                return [1]

            prev_r = pascal_triangle(rows - 1) 
            result.append(prev_r) 
            res = [1]
            for i in range(1, len(prev_r)):
                res.append(prev_r[i] + prev_r[i - 1])  
            res.append(1)    

            return  res  

        result.append(pascal_triangle(numRows - 1))    
        return result
        