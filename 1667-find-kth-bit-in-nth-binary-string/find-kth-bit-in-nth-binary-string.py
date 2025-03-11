class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def reverse(x):
            reversed = []
            for i in range(len(x) - 1, -1, -1):
                if x[i] == '0':
                    reversed.append("1")
                else:    
                    reversed.append("0") 

            return "".join(reversed)        
        

        def helper(n):
            if n == 1:
                return "0"
            x = helper(n - 1)
            return x + "1" + reverse(x) 

        x = helper(n)       
        return x[k - 1]   
        