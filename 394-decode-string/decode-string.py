class Solution:
    def decodeString(self, s: str) -> str:

        stack =  []
        for char in s:
            if char == ']':
                res = []
                while stack and stack[-1] != "[":
                    res.append(stack.pop())
                
                stack.pop()

                nums = []
                while stack and stack[-1].isdigit():
                    nums.append(stack.pop())

                num = int("".join(nums[::-1]))
                res = "".join(res[::-1]) * num   
                stack.append(res) 

            else:
                stack.append(char)
    
        return "".join(stack)         
                
            



        


        