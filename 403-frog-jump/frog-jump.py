class Solution:
    def canCross(self, stones: List[int]) -> bool:

        memo = defaultdict(bool)
        def dp(idx, k):
            index = (idx, k)
            if index in memo:
                return memo[index]

            if stones[idx] == stones[-1]:
                return True
           
            if idx >= len(stones):
                return False
            
            for i in range(idx + 1, len(stones)):
                if stones[i] == stones[idx] + k:
                    if dp(i, k - 1) or dp(i, k) or dp(i, k + 1):
                        memo[index] = True
                        return True

            memo[index] == False
            return memo[index]

        return dp(0, 1)





        