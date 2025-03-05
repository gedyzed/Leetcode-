class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        open_close = {'(' : ')', '[': ']', '{' :'}'}
        for char in s:
            if stack and stack[-1] in open_close and open_close[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)   


        return not len(stack)          



        