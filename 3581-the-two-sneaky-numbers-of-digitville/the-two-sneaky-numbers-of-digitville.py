class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        nums_count, result = {}, []
        for i, num in enumerate(nums):
            if num in nums_count:
                result.append(num)
            nums_count[num] = i
            
        return result        
                  
        