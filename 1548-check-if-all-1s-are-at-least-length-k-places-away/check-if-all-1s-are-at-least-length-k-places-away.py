class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        left = 0
        for right in range(1, len(nums)):
            if nums[right] == 1 and nums[left] == 1:
                if right - left - 1 < k:
                    return False
                left = right
            elif nums[right] == 1 and nums[left] != 1:
                left = right
        
        return True



        