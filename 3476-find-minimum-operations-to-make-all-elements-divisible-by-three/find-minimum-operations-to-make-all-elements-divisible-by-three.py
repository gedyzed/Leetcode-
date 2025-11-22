class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:
            mod = num % 3
            ans += min(mod, 3 - mod)
        
        return ans

        