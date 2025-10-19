class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stones_hash = {}
        for i, stone in enumerate(stones):
            stones_hash[stone] = i

        memo = defaultdict(bool)
        def dp(idx, k):
            index = (idx, k)
            if index in memo:
                return memo[index]

            if stones[idx] == stones[-1]:
                return True
           
            if idx >= len(stones):
                return False
            
            for step in (k - 1, k, k + 1):
                if step > 0:
                    nxt_pos = stones[idx] + step
                    if nxt_pos in stones_hash:
                        i = stones_hash[nxt_pos]
                        if dp(i, step):
                            memo[index] = True
                            return True

            memo[index] == False
            return memo[index]

        if stones[1] != 1:
            return False
        return dp(1, 1)





        