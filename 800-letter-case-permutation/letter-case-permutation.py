class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        for mask in range(1 << n):
            path = []
            for i in range(n):
                if mask >> i & 1:
                    path.append(s[i])
                else:
                    path.append(s[i].swapcase())

            ans.append("".join(path))

        return list(set(ans))             
        

