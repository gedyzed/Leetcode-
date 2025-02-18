class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        left = presum = count = 0
        mod_hash = defaultdict(int)
        mod_hash[0] = 1
        for right in range(len(nums)):
            presum += nums[right]
            x = presum % k
    
            if x in mod_hash:
                count += mod_hash[x]  

            mod_hash[presum % k] += 1  

        return count     


        