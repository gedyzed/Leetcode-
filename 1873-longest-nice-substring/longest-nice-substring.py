class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) <= 1:
            return ""

        letters = set(s)
        for i in range(len(s)):           
            if s[i].swapcase() not in letters:
                l = self.longestNiceSubstring(s[:i])    
                r = self.longestNiceSubstring(s[i+1:])   
                return max(l, r, key=len) 

        return s        





        