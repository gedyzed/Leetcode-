class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1]*(n+1)
        suffix = [1]*(n+1)

        for left,right in enumerate(range(n-1,-1,-1)):
            suffix[right] = suffix[right+1] * nums[right]
            prefix[left] = prefix[left-1] * nums[left]

        ans = [0] * n
        for i in range(n):
            ans[i] = prefix[i-1] * suffix[i+1]

        return ans    
        

 




