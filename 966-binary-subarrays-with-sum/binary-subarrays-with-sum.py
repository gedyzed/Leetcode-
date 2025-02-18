class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        left = count = presum = 0
        sum_hash = defaultdict(int)
        sum_hash[0] = 1
        for right in range(len(nums)):
            
            presum += nums[right]
            count += sum_hash[presum - goal]
            sum_hash[presum] += 1

        return count    
        