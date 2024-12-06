class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort()
        min_ = nums[0]
        operations = count = 0
        for num in nums:
            if min_ != num:
                count += 1
                min_ = num

            operations += count    
            
        return operations        

        