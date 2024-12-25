class Solution:
    def longestOnes(self, s: List[int], k: int) -> int:
        count = left = max_ones = 0
        queue = deque()
        for right in range(len(s)):
            if not s[right]:
                count += 1
                queue.append(right)
                
            if count > k:
                left = queue.popleft() + 1
                count -= 1

            max_ones = max(max_ones,right - left + 1)  

        return max_ones 
        