class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        is_comment = False
        result = []
        for s in source :
            if not is_comment :
                chars = []

            i = 0
            while i < len(s):
            
                if not is_comment and i + 1 < len(s) and s[i: i + 2] == '/*': 
                    is_comment = True
                    i += 1
                elif is_comment and i + 1 < len(s) and s[i: i + 2] == '*/': 
                    is_comment = False
                    i += 1
                elif not is_comment and i + 1 < len(s) and s[i: i + 2] == '//' :
                    break  

                elif not is_comment :
                    chars.append(s[i])
 
                i += 1     
           
            if not is_comment and chars:        
                result.append("".join(chars))       

        return result

        