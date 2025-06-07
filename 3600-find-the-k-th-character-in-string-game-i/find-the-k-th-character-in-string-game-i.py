class Solution:
    def kthCharacter(self, k: int) -> str:

        ans = "a"
        while len(ans) < k:
            gen = ""
            for char in ans:
                if char == "z":
                    gen += "a" 
                else:
                    gen += chr(ord(char) + 1)  

            ans += gen          
            
        return ans[k - 1]    




      
        

        