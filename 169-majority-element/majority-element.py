class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        n = len(nums) // 2
        for k in nums_count:
            if nums_count[k] > n:
                return k
