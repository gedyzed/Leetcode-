class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(s, idx, target):

            if idx >= len(s):
                return self.sum == target

            for i in range(idx, len(s)):
                val = int(s[idx: i + 1])
                if self.sum + val > target:
                    continue
                self.sum += val
                if backtrack(s, i + 1, target):
                    return True
                self.sum -= val  

            return False            
                
        ans = 0
        for i in range(1, n + 1):
            self.sum = 0
            if backtrack(str(i * i), 0, i):
                ans += i * i

        return ans        




        