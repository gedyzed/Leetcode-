class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right ) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        ans = [-1, -1]        
        if 0 <= left < len(nums) and nums[left] == target:
            ans[0] = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right ) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1  

        if 0 <= right < len(nums) and nums[right] == target:
            ans[1] = right     

        return ans               

        
         