class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        left = 0
        substrings = set()
        for right in range(k, len(s) + 1):
            sub = s[left: right]
            substrings.add(sub)
            left += 1
        

        return len(substrings) == 1 << k



        
        