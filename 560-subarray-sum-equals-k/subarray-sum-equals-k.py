class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        left = count = presum = 0
        sum_hash = defaultdict(int)
        sum_hash[0] = 1
        for right in range(len(nums)):
            
            presum += nums[right]
            count += sum_hash[presum - k]
            sum_hash[presum] += 1

        return count    
              