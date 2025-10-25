class Solution:
    def numDecodings(self, s: str) -> int:

        memo = defaultdict(int)
        letters = set([str(num) for num in range(1, 27)])
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == len(s):
                return 1
            
            if idx > len(s):
                return 0

            count = 0 
            for i in range(idx, len(s)):
                letter = s[idx:i + 1]
                if letter not in letters:
                    break

                if letter in letters:
                    count += dp(i + 1)
                
            memo[idx] = count
            return count
        return dp(0)
                
                    
    