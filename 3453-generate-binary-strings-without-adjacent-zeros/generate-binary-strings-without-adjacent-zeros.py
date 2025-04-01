class Solution:
    def validStrings(self, n: int) -> List[str]:

        def backtrack(ones, zeros):

            if len(ans) == n:
                res.append("".join(ans))
                return

            if (zeros <= n - 1 and not ans) or (ans[-1] == '1'):
                ans.append("0")  
                backtrack(ones, zeros + 1)  
                ans.pop()

            if ones < n :
                ans.append("1")   
                backtrack(ones + 1, zeros) 
                ans.pop()


        res, ans = [], []
        backtrack(0, 0)     
        return res   

        