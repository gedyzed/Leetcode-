class Solution:
    def simplifyPath(self, path: str) -> str:
        spath = ""
        stack = []
        counter = 0

        for c in path + "/":
            if c != '/':
                spath += c 
            elif c == '/' and len(spath):
                if spath == ".." and stack:
                    stack.pop()
                elif spath != '.' and spath != "..":
                    stack.append(spath)
                spath = ""    
        
        if not len(stack):
            return '/'
        spath = ""   
        for i in range(len(stack)):
            spath += "/" + stack[i]
            
        return  spath   
               

        