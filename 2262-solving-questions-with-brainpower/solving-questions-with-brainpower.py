class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        memo = defaultdict(int)
        def dp(idx):

            if idx in memo:
                return memo[idx]
            
            if idx >= len(questions):
                return 0
            
            num, skip = questions[idx]
            memo[idx] = max(num + dp(idx + skip + 1), dp(idx + 1))
            return memo[idx]
        return dp(0)
        