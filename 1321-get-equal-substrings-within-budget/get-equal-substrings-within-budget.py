class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = cost = max_len = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left])) 
                left += 1

            max_len = max(max_len, right - left + 1)   

        return max_len      





        