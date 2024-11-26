class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands = []
        num = num2 = 0
        operator = "+-*/"
        for token in tokens:
            if token in operator:
                if token == "*" and len(operator) >= 2:
                    num = operands.pop() * operands.pop()
                elif token == "/" and len(operator) >= 2:
                    num2 = operands.pop()
                    num = operands.pop()
                    num = int(num / num2)
                elif token == "-" and len(operator) >= 2:
                    num2 = operands.pop()
                    num = operands.pop()
                    num = num - num2
                elif token == "+" and len(operator) >= 2:
                    num = operands.pop() +  operands.pop()   
                operands.append(num)          
            else:
                operands.append(int(token))   
 
        return operands[0]         

                







    
  
        print(operators, operands)                  

        