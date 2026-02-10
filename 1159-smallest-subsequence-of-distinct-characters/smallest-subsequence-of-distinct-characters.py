class Solution:
    def smallestSubsequence(self, s: str) -> str:

        letters = Counter(s)
        stack = []
        added = set()
        for ch in s:
            letters[ch] -= 1
            while stack and stack[-1] > ch and letters[stack[-1]] and ch not in added:
                popped = stack.pop()
                added.remove(popped)
            
            if ch not in added:
                stack.append(ch)
                added.add(ch)
               
        return "".join(stack)
        