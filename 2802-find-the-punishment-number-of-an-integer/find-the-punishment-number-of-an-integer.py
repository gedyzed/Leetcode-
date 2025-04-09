class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(s, idx, target):

            if idx >= len(s):
                return sum(curr) == target

            for i in range(idx, len(s)):
                val = int(s[idx: i + 1])
                if curr and curr[-1] + val > target:
                    continue
                curr.append(val) 
                if backtrack(s, i + 1, target):
                    return True
                curr.pop()    

            return False            
                

        squares = [(i, str(i * i)) for i in range(1, n + 1)]
        ans = 0
        for target, square in squares:
            curr = []
            if backtrack(square, 0, target):
                ans += target * target
                
        return ans        



        