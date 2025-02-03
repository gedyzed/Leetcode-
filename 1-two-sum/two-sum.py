class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_index = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in value_index:
                return [i, value_index[x]]    
            value_index[num] = i
           
           

            
            
        