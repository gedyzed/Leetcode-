class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        result = []
        for char in command:
            if char == ')' and stack:
                if stack[-1] == '(':
                    result.append('o')
                else: 
                    result.append('al')    
            elif char == 'G' :
                result.append('G')
            else:
                stack.append(char)  
                  
        return "".join(result)        
                
        