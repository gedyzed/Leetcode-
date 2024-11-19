class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = left = maxf = 0
        letters = defaultdict(int)
        for right in range(len(s)):
            letters[s[right]] += 1
            if letters[s[right]] > maxf:
                maxf = letters[s[right]]
                
            while k < (right - left + 1 - maxf):
                letters[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1) 
         
        return max_length    

                

