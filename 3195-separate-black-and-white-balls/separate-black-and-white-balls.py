class Solution:
    def minimumSteps(self, s: str) -> int:

        ones = swaps = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            elif ones and s[i] == '0':
                swaps += ones
                
        return swaps         
                 

        