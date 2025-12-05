class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        total = sum(nums)
        count = curr_sum = 0
        for num in nums:
            total -= num
            if not total:
                break
            curr_sum += num
            if not abs(total - curr_sum) & 1:
                count += 1
        
        return count


        