class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_subs = left = 0
        letters = defaultdict(int)

        for right in range(len(s)):
            letters[s[right]] += 1
            while letters[s[right]] > 1:
                letters[s[left]] -= 1
                left += 1

            longest_subs = max(longest_subs, right - left + 1) 
             
        return longest_subs      
        