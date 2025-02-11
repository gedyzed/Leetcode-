class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        part, n = list(part), len(part)
        stack = []

        for i in range(len(s) + 1):
            
            if i >= n - 1 and stack[-n:] == part:
                for _ in range(n):
                    stack.pop()

            if i < len(s):
                stack.append(s[i]) 

        return "".join(stack)   

        