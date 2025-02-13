class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = set()
        max_length = left = 0 

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1

            letters.add(s[right])
            max_length = max(max_length, right - left + 1) 

        return max_length       

            
        