class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort()
        operations = count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
            operations += count    
            
        return operations        

        