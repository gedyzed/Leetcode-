class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i, ans = 0, []
        while i < len(nums):
            if nums[i] - 1 != i and nums[nums[i] - 1] != nums[i]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]  
            else:    
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(i + 1)
                  
        return ans            

        