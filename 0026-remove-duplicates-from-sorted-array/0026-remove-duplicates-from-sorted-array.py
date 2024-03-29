class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        first = 0
        second = 1

        while second < len(nums):
            if nums[first] == nums[second]:
                nums.remove(nums[second])
            else:
                first = second
                second += 1

        return len(nums)        


        