class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack1, stack2 = [], []
        for char in s:
            if stack1 and char == '#':
                stack1.pop()
            elif char != '#':
                stack1.append(char) 

        for char in t:
            if stack2 and char == '#':
                stack2.pop()
            elif char != '#':
                stack2.append(char)

        if ''.join(stack1) == ''.join(stack2):
            return True
        return False                
        

        

    







        