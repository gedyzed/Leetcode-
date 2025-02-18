class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        left = count = presum = 0
        sum_hash = defaultdict(int)
        for right in range(len(nums)):
            presum += nums[right]
            x = presum - k

            if x in sum_hash:
                count += sum_hash[x]

            if presum == k:
                count += 1     

            sum_hash[presum] += 1

        return count    
              