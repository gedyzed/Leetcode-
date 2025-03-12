class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if not rowIndex:
            return [1]

        result = []
        res = [1, 1]
        for i in range(rowIndex):
        
            for j in range(1, len(result)):
                res[j] = result[j] + result[j - 1]
            
            result = res    
            res = [1] * (len(result) + 1)

        return result        


      
