class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(idx, res):
       
            if self.sum == target:
                result.append(res[:])
                
            if self.sum >= target:
                return

            for i in range(idx, len(candidates)):
                res.append(candidates[i])    
                self.sum += res[-1]  
                backtrack(idx, res)
                idx += 1
                self.sum -= res.pop()    

        self.sum = 0
        result = []
        backtrack(0, [])
        return result






        