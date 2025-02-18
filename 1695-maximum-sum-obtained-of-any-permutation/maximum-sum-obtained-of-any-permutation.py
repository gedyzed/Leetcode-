class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        count = [0] * (len(nums) + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1

        presum = 0
        for i in range(len(nums)):
            count[i] += presum
            presum = count[i]
        
        nums = sorted(nums, reverse=True)
        count = sorted(count, reverse=True)

        result = 0
        for i, num in enumerate(nums):
            result += count[i] * num

        return result % (10 ** 9 + 7)    
       

            

            

