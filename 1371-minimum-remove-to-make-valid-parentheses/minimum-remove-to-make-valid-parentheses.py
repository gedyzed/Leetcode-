class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack1, stack2 = [], []
        for i in range(len(s)):
            if stack1 and stack1[-1] == '(' and s[i] == ')':
                stack1.pop()
                stack2.append(s[i])
            elif s[i] != ')':
                stack2.append(s[i])
                if s[i] == '(':
                    stack1.append(s[i])
        print(stack1, stack2)
        i = len(stack2) - 1
        while stack1 :
            if stack1[-1] == stack2[i]:
                stack2[i] = ""
                stack1.pop()
            i -= 1

        return "".join(stack2)            
     
        