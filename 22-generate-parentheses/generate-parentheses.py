class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack():

            if len(ans) >= 2 * n:
                res.append("".join(ans))
                return 

            if count['('] < n:
                ans.append('(') 
                count['(']  += 1
                backtrack()  
                count[ans.pop()] -= 1

            if count[')'] < count['(']:
                ans.append(')') 
                count[')']  += 1
                backtrack()  
                count[ans.pop()] -= 1

               
        count = {'(': 0, ')': 0}
        ans, res = [], []
        backtrack()
        return res
        

        