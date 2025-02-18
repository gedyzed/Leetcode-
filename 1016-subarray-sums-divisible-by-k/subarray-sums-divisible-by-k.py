class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        left = presum = count = 0
        sum_hash = defaultdict(int)
        sum_hash[0] = 1
        for right in range(len(nums)):
            presum += nums[right]
            x  = presum % k
    
            if x in sum_hash:
                count += sum_hash[x]  

            sum_hash[presum % k] += 1  

        return count     


        