class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = [0] 
        for operand in operations:
            if operand == 'C':
                stack.pop()
            elif operand == 'D' :
                stack.append(stack[-1]*2)   
            elif operand == '+' :
                stack.append(stack[-1]+ stack[-2])  
            else :
                stack.append(int(operand))      

        return sum(stack) 
        