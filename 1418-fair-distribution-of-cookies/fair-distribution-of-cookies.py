class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def backtrack(idx):

            if idx >= len(cookies):
                self.min = min(self.min, max(childs))
                return 
                
            if self.min < max(childs):
                return    

            for i in range(k):
                childs[i] += cookies[idx]
                backtrack(idx + 1)
                childs[i] -= cookies[idx]

                if not childs[i]:
                    break

        
        self.min = float('inf')
        self.res = max(cookies)
        childs = [0] * k   
        backtrack(0)  
        return self.min   

        