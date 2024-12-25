class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack, closing  = [], 0
        
        for char in s:
            if stack and char == ')':
                stack.pop()
            elif char == '(':
                stack.append(char)    
            elif not stack :
                closing += 1

        return closing + len(stack) 
        