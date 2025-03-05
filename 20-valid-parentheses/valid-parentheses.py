class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing = [')', ']', '}']
        for char in s:
            if stack and stack[-1] == '(' and char == closing[0]:
                stack.pop()
            elif stack and stack[-1] == '[' and char == closing[1]:
                stack.pop()
            elif stack and stack[-1] == '{' and char == closing[2]:
                stack.pop()
            else:
                stack.append(char)   

        return not len(stack)          



        