class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        first = 0 # pointer to first element
        second = 1 #pointer to second element

        while second < len(nums):
            if nums[first] == nums[second]:
                nums.pop(second) #removes element at index second
            else:
                first = second
                second += 1

        return len(nums)        


        