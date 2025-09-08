class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        nums = set()
        for num in range(n):
            x = n - num                                               
            if "0" in str(num) or "0" in str(x):
                continue

            if x in nums:
                return [x, num]
            elif num + num == n:
                return [num, num]
            nums.add(num)   

        return []






          
       


        