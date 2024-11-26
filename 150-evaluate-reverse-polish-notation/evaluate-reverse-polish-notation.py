class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands = []
        num = num2 = 0
        for token in tokens:
            if token in "+-*/":
                if token == "*":
                    num = operands.pop() * operands.pop()
                elif token == "/" :
                    num2 = operands.pop()
                    num = operands.pop()
                    num = int(num / num2)
                elif token == "-":
                    num2 = operands.pop()
                    num = operands.pop()
                    num = num - num2
                elif token == "+":
                    num = operands.pop() +  operands.pop()   
                operands.append(num)          
            else:
                operands.append(int(token))   
 
        return operands[0]         

                            

        