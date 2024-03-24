class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
    
        while first <= last:
            midpoint = (last + first)//2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                first = midpoint +1
            else: 
                last = midpoint - 1    
        return first        

                   

            
                        





         


        