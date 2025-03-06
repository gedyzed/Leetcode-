class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_queue = deque()
        min_queue = deque()

        left = max_len = 0
        for right in range(len(nums)):
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop() 

            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()   

            max_queue.append(nums[right])  
            min_queue.append(nums[right])

            if max_queue[0] - min_queue[0] > limit:
                value = nums[left]
                if value == max_queue[0]:
                    max_queue.popleft()
                if value == min_queue[0]:
                    min_queue.popleft()
                left += 1

            if max_queue and min_queue:
                max_len = max(max_len, right - left + 1)

        return max_len           





        