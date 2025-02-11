class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        part, n = list(part), len(part)
        stack = list(s[:n])
        for i in range(n, len(s)):
            if stack[-n:] == part:
                stack = stack[:-n]
            stack.append(s[i]) 

        if stack[-n :] == part: 
            stack = stack[:-n]      

        return "".join(stack)   

        