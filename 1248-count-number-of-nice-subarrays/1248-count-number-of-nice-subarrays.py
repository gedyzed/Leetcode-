class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans, left, que = 0, -1, deque()
        for i in range(len(nums)):
            if nums[i]%2:
                que.append(i)
                if len(que) > k:
                    left = que.popleft()
            if len(que) == k:
                ans += que[0]-left
        return ans
        