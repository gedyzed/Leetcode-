class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count = start = 0
        validIndex = -1
        for end in range(len(nums)):
            if nums[end] > right:
                start = end + 1 
            elif left <= nums[end] <= right:
                validIndex = end
            count += max(0, validIndex - start + 1)
        return count

            

            
                

    





            




        


        