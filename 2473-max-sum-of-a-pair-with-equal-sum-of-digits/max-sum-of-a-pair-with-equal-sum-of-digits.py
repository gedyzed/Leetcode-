class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digit_sum = defaultdict(list)
        for i, num in enumerate(nums):
            dgt_sum = sum(int(n) for n in str(num)) 
            digit_sum[dgt_sum].append(num)

        nums = [v for v in digit_sum.values() if len(v) > 1]  

        max_sum = -1
        for num in nums:
            num = sorted(num)
            max_sum = max(max_sum, sum(num[-2:]))

        return max_sum    



            


       
        