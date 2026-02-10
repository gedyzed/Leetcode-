class Solution:
    def smallestSubsequence(self, s: str) -> str:

        letters = Counter(s)
        stack = []
        visited = set()
        for ch in s:
            letters[ch] -= 1
            if ch in visited:
                continue

            while stack and stack[-1] > ch and letters[stack[-1]]:
                popped = stack.pop()
                visited.remove(popped)
            
            stack.append(ch)
            visited.add(ch)
               
        return "".join(stack)
        