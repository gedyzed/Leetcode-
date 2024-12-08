class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def binarySearch(num, left , right, nums):
            len_ = 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= num:
                    len_ = mid + 1
                    left += 1
                elif nums[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            return len_       

        result = []
        nums.sort()
        n = len(nums)
        presum = [0] * n
        
        for i in range(n):
            presum[i] = presum[i - 1] + nums[i]

        for q in queries:
            result.append(binarySearch(q,0, n - 1, presum))

        return result    
 