class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substring):
            unique = set(substring)
            for char in unique:
                if char.lower() not in unique or char.upper() not in unique:
                    return False
            return True

        max_sub = ""   
        n = len(s)

        for left in range(n):
            for right in range(left + 1, n + 1):
                substring = s[left : right]
                if is_nice(substring) and len(substring) > len(max_sub):
                    max_sub = substring
                    
        return max_sub             

            
              


        