class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        def countSorting(nums):
            countArray = [0] * 101

            for num in nums:
                countArray[num] += 1

            result = [] 
            for i, count in enumerate(countArray):
                result.extend([i] * count)  

            return result     

        nums_ = countSorting(nums)
        num_smaller = {}

        for i in range(len(nums_)):
            if nums_[i] not in num_smaller:
                num_smaller[nums_[i]] = i

        return [num_smaller[num] for num in nums ]
        