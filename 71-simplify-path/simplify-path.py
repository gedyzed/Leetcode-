class Solution:
    def simplifyPath(self, path: str) -> str:

        spath = ""
        stack = []

        for c in path + "/":
            if c != '/':
                spath += c 
            elif c == '/' and len(spath):
                if spath == ".." and stack:
                    stack.pop()
                elif spath != '.' and spath != "..":
                    stack.append(spath)
                spath = ""    
            
        return "/" + "/".join(stack)  
               

        