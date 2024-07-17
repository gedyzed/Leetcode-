class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rightsum = sum(nums)
        leftsum = 0

        for i in range(len(nums)):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]

        return -1        

    


        
        
        
                
                



            
        