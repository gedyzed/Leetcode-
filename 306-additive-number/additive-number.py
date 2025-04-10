class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        if len(num) <= 2:
            return False

        def backtrack(idx):

            if idx == len(num):
                return len(res) > 2

            for i in range(idx, len(num)):
                val = num[idx: i + 1]
                if len(val) > 1 and val[0] == '0':
                    continue
                if len(res) > 1 and res[-1] + res[-2] != int(val):
                    continue

                res.append(int(val))
                if backtrack(i + 1):
                    return True
                res.pop()    

            return False  

        res = []
        return backtrack(0)          

                  
        