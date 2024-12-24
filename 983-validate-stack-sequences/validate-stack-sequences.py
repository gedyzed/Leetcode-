class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped.reverse()
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while popped and stack and popped[-1] == stack[-1]:
                stack.pop()
                popped.pop()

        return not len(stack)          
        