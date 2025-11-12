class Solution:
    def myPow(self, x: float, n: int) -> float:

        result = 1
        exp = abs(n)
        while exp > 0:
            if exp & 1:
                result *= x
            x *= x
            exp >>= 1
        
        return result if n >= 0 else 1 / result
        