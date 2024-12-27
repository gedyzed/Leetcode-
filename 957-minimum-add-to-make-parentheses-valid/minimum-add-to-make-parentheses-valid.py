class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        
        for char in s:
            if stack and char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)    

        return len(stack) 
        