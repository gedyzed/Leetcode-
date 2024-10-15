class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        left = 0
        answer = ""
        for right in range(len(s)):
            if "(" == s[right]: stack.append('(')
            elif stack and stack[-1] == '(': stack.pop()
            if len(stack) == 0:
                answer += s[left+1:right]
                left = right + 1 
        return answer        

        