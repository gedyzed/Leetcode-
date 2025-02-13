class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = defaultdict(int)
        max_length = left = 0 

        for right in range(len(s)):
            letters[s[right]] += 1

            while letters[s[right]] > 1:
                letters[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1) 
            
        return max_length       

            
        