class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = {}
        max_length = left = 0 

        for right in range(len(s)):

            if s[right] in letters:
                left = max(left, letters[s[right]] + 1)
                  
            max_length = max(max_length, right - left + 1) 
            letters[s[right]] = right
            
        return max_length       

            
        