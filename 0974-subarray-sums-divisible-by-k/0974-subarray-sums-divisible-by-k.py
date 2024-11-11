class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums) 
        reminder_to_count = {0:1}
        count = 0
        presum = [0] * n
        
        for i in range(n):
            presum[i] = nums[i] + presum[i - 1] 
            reminder = presum[i] % k
            if reminder in reminder_to_count:
                count += reminder_to_count[reminder] 
                reminder_to_count[reminder] += 1    
            else:
                reminder_to_count[reminder] = 1    

        return count                    