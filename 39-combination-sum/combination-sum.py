class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(idx, res):
       
            if self.sum == target:
                result.append(res[:])
                
            if self.sum >= target:
                return

            for i in range(len(candidates)):
                res.append(candidates[i])    
                self.sum += res[-1]  
                backtrack(i + 1, res)
                self.sum -= res.pop()    

        self.sum = 0
        result = []
        backtrack(0, [])

        ans = []
        for r in result:
            r = sorted(r)
            if r not in ans:
                ans.append(r)

        return ans






        