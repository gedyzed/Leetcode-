class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtrack(idx):

            if idx == len(s):
                if len(res) == 4:
                    result.append(".".join(res[:]))
                return 

            for i in range(idx, len(s)):
                ip = s[idx: i + 1]
                if int(ip) > 255 or len(res) >= 4 or (len(ip) > 1 and ip[0] == '0'):
                    return
                res.append(ip)    
                backtrack(i + 1)
                res.pop()

        result, res = [], []
        backtrack(0)
        return result
        