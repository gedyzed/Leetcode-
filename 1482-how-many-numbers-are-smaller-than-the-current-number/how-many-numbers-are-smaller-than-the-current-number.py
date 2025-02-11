class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_ = [num for num in nums]
        nums_.sort()
        num_smaller, count = {}, 1
        num_smaller[nums_[0]] = 0

        for i in range(1, len(nums_)):
            if nums_[i] != nums_[i - 1]:
                num_smaller[nums_[i]] = count
            count += 1

        return [num_smaller[num] for num in nums ]
        