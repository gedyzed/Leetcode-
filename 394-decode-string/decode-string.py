class Solution:
    def decodeString(self, s: str) -> str:

        def decode(i):

            res = ""
            num = 0

            while i < len(s):

                if s[i].isdigit():
                    num = num * 10 + int(s[i]) 
                elif s[i] == '[':
                    substr, i = decode(i + 1)   
                    res += num * substr
                    num = 0

                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]

                i += 1
            return res, i

        return decode(0)[0]
                
            



        


        