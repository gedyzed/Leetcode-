class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        num, ans = 0, []
        for bit in nums:
            num = (num << 1) | bit
            num %= 5
            ans.append(num == 0)
            
        return ans

            
            
