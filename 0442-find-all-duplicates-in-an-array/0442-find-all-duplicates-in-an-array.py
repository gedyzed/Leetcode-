class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        duplicates = []
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            elif nums[i] == nums[correct] and correct != i: 
                if nums[i] not in duplicates:
                    duplicates.append(nums[i])
                i += 1                        
            else:
                i += 1

        return duplicates         

        