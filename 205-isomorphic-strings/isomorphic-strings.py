class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            if s[i] not in map_st and t[i] not in map_ts :
                map_st[s[i]] = t[i]
                map_ts[t[i]] = s[i]

        for i in range(len(s)):
           if s[i] not in map_st or map_st[s[i]] != t[i]:
                return False
        return True        

            

            
    

        



     






        


        