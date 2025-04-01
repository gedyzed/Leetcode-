class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def validate(max_sum):
            sum_, split = 0, 1
            for num in nums:
                if sum_ + num > max_sum:
                    sum_ = 0
                    split += 1    
                sum_ += num

            return split <= k  

        low, high = max(nums), sum(nums)   
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low            



                    
        