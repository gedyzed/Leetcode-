class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/") 
        stack = []

        for c in path:
            if c  == "..":
                if stack: 
                    stack.pop() 
            elif c != '.' and c != "":
                stack.append(c)

        return "/" + "/".join(stack)  
               

        