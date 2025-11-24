class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        num = nums[0]
        ans = [False if nums[0] else True]
        for i in range(1, len(nums)):
            num <<= 1
            if nums[i]:
                num |= 1

            num %= 5
            if not num:
                ans.append(True)
            else:
                ans.append(False)
            
            
        
        return ans

            
            
