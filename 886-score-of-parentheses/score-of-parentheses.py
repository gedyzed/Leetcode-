class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        val = score = 0
        for c in s:
            val = 0
            if c == '(':
                stack.append(0)
            else :
                while stack and stack[-1] != 0:
                    val += stack.pop()  
                val = max(2 * val, 1)  
                stack.pop() 
                stack.append(val)

        while stack:
            score += stack.pop() 
            
        return score
        