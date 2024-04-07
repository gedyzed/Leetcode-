class Solution:
    def makeGood(self, s: str) -> str:

        right = len(s)-1
        left = right -1

        while left >= 0 :
            if s[left] != s[right]:
                if s[left].upper () == s[right] or s[left] == s[right].upper():
                    s = s[:left] + s[right+1:]
                    right = len(s)
                    left = right -1
            right = left
            left -= 1                  
           
        return s        

            







        