class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        presum_to_count = {0 : 1}
        current = 0
        count = 0
        for num in nums :
            current += num
            count += presum_to_count.get(current - k, 0)
            presum_to_count[current] = 1 + presum_to_count.get(current, 0)
        
        return  count       


        
        
        
        