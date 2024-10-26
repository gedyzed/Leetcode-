class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_chars(st):
            stack = []
            for char in st:
                if stack and char == '#':
                    stack.pop()
                elif char != '#':
                    stack.append(char)    
            return stack 
  
        return remove_chars(s) == remove_chars(t)

        

        

    







        