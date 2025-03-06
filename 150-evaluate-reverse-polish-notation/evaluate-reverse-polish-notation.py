class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        oper = {"+", '*', '-', '/'}
        stack = []
        for token in tokens:
            if token not in oper:
                stack.append(int(token))  

            else:   
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)  
                elif token == '*':
                    stack.append(num1 * num2)   
                else:

                    stack.append(int(num2 / num1))
                

        return stack[-1] 
              

           







        