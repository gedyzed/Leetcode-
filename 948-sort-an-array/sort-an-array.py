class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        max_, min_ = max(nums), min(nums)
        countArray = [0] * (max_ - min_ + 1)

        for num in nums:
            countArray[num - min_] += 1

        result = []
        for i, count in enumerate(countArray):
            if not count:
                continue
            result.extend([i + min_] * count) 

        return result   

        