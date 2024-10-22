class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1
        duplicates = []      
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(i + 1)
                
        return duplicates        


        