class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers

        left = 0 
        right = len(nums) -1

        indices = []

        while left < right:
            if nums[left] + nums[right] == target:
                indices.append(left+1)
                indices.append(right+1)
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target: 
                right -= 1
            else: left += 1

        return indices          

        