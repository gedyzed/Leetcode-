class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def pow_(x, n, m):
            result, exp = 1, n
            x = x % m
            while exp > 0:
                if exp & 1:
                    result = (result * x) % m
                x = x * x % m
                exp >>= 1
            
            return result

        mod = 10 ** 9 + 7
        ans, exp = 0, n // 2
        if n & 1:
            ans = pow_(4, exp, mod) * pow_(5, exp + 1, mod)
        else:
            ans = pow_(4, exp, mod) * pow_(5 , exp, mod)
        
        return ans % mod
            