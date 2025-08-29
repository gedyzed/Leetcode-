class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        even_n = even_m = 0
        odd_n = odd_m = 0

        for num in range(1, max(n, m) + 1): 

            if num % 2 == 0:
                if num <= n:
                    even_n += 1
                if num <= m:
                    even_m += 1
            else:
                if num <= n:
                    odd_n += 1
                if num <= m:
                    odd_m += 1

        ans = even_n * odd_m  + odd_n * even_m
        return ans     
       