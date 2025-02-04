class Solution:
    def minSteps(self, s: str, t: str) -> int:

        count = 0
        s = Counter(s)
        t = Counter(t)

        for k, v in s.items():
            if t[k] < s[k]:
                count += v - t[k]      
        return count           
    
        