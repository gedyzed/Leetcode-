class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for c in s:
            stack.append(c)
            if c == "*":
                stack.pop() 
                stack.pop()   

        return "".join(stack)

        