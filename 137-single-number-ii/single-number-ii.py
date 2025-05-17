class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        for key in nums_count:
            if nums_count[key] == 1:
                return key
                


        