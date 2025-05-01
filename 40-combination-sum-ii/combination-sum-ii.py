class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(idx, total):

            if total >= target:
                if total == target:
                    result.append(res[:])
                return  

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                res.append(candidates[i])  
                backtrack(i + 1, total + candidates[i])
                res.pop() 

        result, res = [], []   
        candidates.sort()
        backtrack(0, 0)
        return result     




        
        