class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder_map = {0: -1}  
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
                
        return False


        