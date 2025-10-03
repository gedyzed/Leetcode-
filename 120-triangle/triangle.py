class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = defaultdict(int)
        def dp(idx, i):

            if (idx, i) in memo:
                return memo[(idx, i)]
            
            if idx == len(triangle):
                return 0
            
            if i == len(triangle[idx]):
                return float("inf")

            res = float("inf")
            num = triangle[idx][i]
            res = min(res, dp(idx + 1, i + 1) + num, dp(idx + 1, i) + num)
            memo[(idx, i)] = res
            return res
            
        return dp(0, 0)
            


        