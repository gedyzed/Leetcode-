class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for char in s:
            s = s[1:] + char
            if s == goal:
                return True
        return False        


        