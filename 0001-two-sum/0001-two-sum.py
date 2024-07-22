class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_to_indices = defaultdict(int)
        x = 0
        ans = []
        for i in range(len(nums)):
            x = target - nums[i]
            if x in value_to_indices:
                return [i,value_to_indices[x]]
            value_to_indices[nums[i]] = i   
                
                 
        
          
               
        