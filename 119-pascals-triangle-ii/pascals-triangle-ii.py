class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if not rowIndex:
            return [1]

        previous_r = self.getRow(rowIndex - 1)
        res = [1]
        for j in range(1, len(previous_r)):
            res.append(previous_r[j] + previous_r[j - 1])
        res.append(1)    
    
        return res        


      
