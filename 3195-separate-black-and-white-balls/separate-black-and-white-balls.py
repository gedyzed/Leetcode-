class Solution:
    def minimumSteps(self, s: str) -> int:

        ones = swaps = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            else:
                swaps += ones
                
        return swaps         
                 

        