class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = s.split()
        max_length = len(max(s, key=len))
        result = [[]  for _ in range(max_length)]

        for i in range(len(s)):
            for j, char in enumerate(s[i]):
                result[j].append(char)
    
            for k in range(j + 1, len(result)):
                result[k].append(" ")     

        for i, r in enumerate(result):
            result[i] = "".join(r).rstrip()   

        return result        




        