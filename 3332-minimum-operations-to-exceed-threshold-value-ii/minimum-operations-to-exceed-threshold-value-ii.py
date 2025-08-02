class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapify(nums)
        count = 0
        while nums and nums[0] < k:
            min_ = heappop(nums)
            val = 0
            if nums:
                max_ = heappop(nums)
                val = 2 * min_ + max_
            else:
                val = 2 * min_ + min_

            heappush(nums, val)
            count += 1   

        return count     






        