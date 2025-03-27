class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def validate(k):
            z_count = 0
            presum = [0] * (len(nums) + 1)
            for i in range(k):
                left, right, val = queries[i] 
                presum[left] += val
                presum[right + 1] -= val
                
            for i in range(1, len(presum)):
                presum[i] += presum[i - 1] 
                if nums[i - 1] - presum[i - 1] <= 0:
                    z_count += 1

            return z_count == len(nums)
        
        left, right = 0, len(queries)
        while left <= right:
            mid = (left + right) // 2
            if validate(mid):
                right = mid - 1
            else:
                left = mid + 1

        if left > len(queries) :
            return -1
        return left             
   
      






        

        