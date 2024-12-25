class Solution:
    def longestOnes(self, s: List[int], k: int) -> int:
        count = left = max_ones = 0
        for right in range(len(s)):
            if not s[right]:
                count += 1
            while count > k:
                if not s[left]:
                    count -= 1
                left += 1

            max_ones = max(max_ones,right - left + 1)  

        return max_ones 
        