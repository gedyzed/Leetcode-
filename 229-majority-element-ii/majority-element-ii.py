class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        n = len(nums) // 3
        result = []
        for k in nums_count:
            if nums_count[k] > n:
                result.append(k)
                
        return result        