class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum_, result = 0, []
    
        for char in s:
            ch = str(ord(char) - 96)
            result.append(ch)
            
        result = "".join(result)     
        for i in range(k):
            result = list(str(result)) 
            result = list(map(int, result)) 
            sum_ = result = sum(result)   

        return sum_    
            
          

        