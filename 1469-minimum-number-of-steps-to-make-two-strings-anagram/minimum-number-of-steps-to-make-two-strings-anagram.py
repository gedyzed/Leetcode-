class Solution:
    def minSteps(self, s: str, t: str) -> int:

        count = 0
        s, t = Counter(s), Counter(t)
        for k, v in s.items():
            if t[k] < s[k]:
                count += v - t[k]      
        return count           
    
        