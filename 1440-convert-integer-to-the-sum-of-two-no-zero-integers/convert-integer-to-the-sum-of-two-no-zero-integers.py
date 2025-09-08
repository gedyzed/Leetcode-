class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        nums = set()
        for num in range(n):
            x = n - num                                               
            if "0" not in str(num) and "0" not in str(x):
                return [num, x]

           






          
       


        