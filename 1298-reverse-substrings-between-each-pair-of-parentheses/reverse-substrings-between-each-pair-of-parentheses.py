class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                portion = []
                while stack[-1] != '(':
                    portion.append(stack.pop())
                stack.pop()    
                stack.extend(portion)
            else:
                stack.append(char)    

        return "".join(stack)        

      
                         



        
            

        
        