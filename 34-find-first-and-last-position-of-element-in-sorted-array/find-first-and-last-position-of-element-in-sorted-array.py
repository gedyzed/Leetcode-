class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 

        ans = [-1, -1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        if left < len(nums) and nums[left] == target and right >= 0:
            ans = [left, right]

        return ans            

        
         