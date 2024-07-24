class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        current_sum = 0
        count = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        
        for num in nums:
            current_sum += num
            if (current_sum - goal) in sum_freq:
                count += sum_freq[current_sum - goal]
            sum_freq[current_sum] += 1
        
        return count                     
                         

