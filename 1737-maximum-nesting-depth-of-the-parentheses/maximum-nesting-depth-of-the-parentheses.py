class Solution:
    def maxDepth(self, s: str) -> int:

        stack, max_ = [], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()    
            max_ = max(len(stack), max_) 

        return max_    
        