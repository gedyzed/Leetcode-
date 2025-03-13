class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        for par in s:
            if par == "(":
                stack.append(0)
            else:
                val = 0
                while stack and stack[-1] != 0:
                    val += stack.pop()

                val = max(2 * val, 1)
                stack[-1] += val
                      
        return sum(stack)

        