class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.rsplit(' ')
        n = len(words)
        s = ""
        for i in range(n-1,-1,-1):
            if '' != words[i]: 
                if s == "":
                    s += words[i] 
                else :
                    s += " " + words[i]    
        return s      

        