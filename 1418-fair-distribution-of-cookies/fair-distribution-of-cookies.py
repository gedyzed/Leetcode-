class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def backtrack(idx, max_):


            if idx >= len(cookies):
                self.min = min(self.min, max_)
                return 
            if self.min <= max_:
                return    
                
            for i in range(k):
                childs[i] += cookies[idx]
                backtrack(idx + 1,  max(max_, childs[i]))
                childs[i] -= cookies[idx]

                if not childs[i]:
                    break

        
        self.min = float('inf')
        childs = [0] * k   
        backtrack(0, 0)  
        return self.min   

        