class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for num in range(n + 1):
            count = 0
            while num: 
                mod = num % 2 
                if mod:
                    count += 1
                num //= 2  
            
            res.append(count)  

        return res       
      
        