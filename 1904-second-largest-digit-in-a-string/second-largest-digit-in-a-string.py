class Solution:
    def secondHighest(self, s: str) -> int:

        s = list(set(s))
        nums = []
        for char in s:
            if char.isdigit():
                nums.append(int(char))

        if len(nums) <= 1:
            return -1 

        nums.sort()    
        return nums[-2]  
           

         


        