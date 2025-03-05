class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def cleanText(s):     
            stack = []
            for char in s:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)

            return stack
            
        return cleanText(s) == cleanText(t)           

   
        