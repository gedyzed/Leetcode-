class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = max_cost = left = 0
        for right in range(len(s)):
            max_cost += abs(ord(s[right]) - ord(t[right]))
            while max_cost > maxCost:
                max_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)  

        return max_length     



        