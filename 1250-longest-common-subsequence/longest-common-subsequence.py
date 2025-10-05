class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for idx1 in range(len(text1) - 1, -1, -1):
            for idx2 in range(len(text2)- 1, -1, -1):
                if text1[idx1] == text2[idx2]:
                    dp[idx1][idx2] = 1 + dp[idx1 + 1][idx2 + 1]
                else:
                    dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])

        return dp[0][0]
            
             