class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        left_count = defaultdict(int)
        for i in range(len(nums)):
            left_count[nums[i]] += 1
            nums_count[nums[i]] -= 1
            left = i - left_count[nums[i]] + 1 
            right = len(nums) - nums_count[nums[i]] - i - 1
            if left_count[nums[i]] > left and nums_count[nums[i]] > right:
                return i

        return -1        

        