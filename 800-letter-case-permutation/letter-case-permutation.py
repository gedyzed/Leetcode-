class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        n = len(s)
        def backtrack(idx):

            if len(res) == n:
                result.append("".join(res))
                return 
    
            res.append(s[idx])
            backtrack(idx + 1)
            res.pop()

            if s[idx].isalpha():
                res.append(s[idx].swapcase())
                backtrack(idx + 1)
                res.pop() 

        result, res = [], []
        backtrack(0)
        return result    


          


        

