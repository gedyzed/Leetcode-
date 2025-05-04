class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        set1 = set(nums)
        for num in range(0, len(nums) + 1):
            if num not in set1:
                return num



       



         

       
                
        