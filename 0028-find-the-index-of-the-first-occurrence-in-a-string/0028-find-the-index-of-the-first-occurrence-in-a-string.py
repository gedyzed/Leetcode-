class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        first = 0 #track the index of haystack
        second = 0  #track the index of needle

        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        
        ans = ""

        while  second < lenNeedle and first < lenHaystack-lenNeedle+1:
            
            if haystack[first + second] == needle[second]:
                        ans += needle[second]
                        print(ans)
                        second += 1
                        if ans == needle:
                            return first                        
            else : 
                 ans = ""  
                 first += 1
                 second = 0
        return -1   


        