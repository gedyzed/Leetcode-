class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a, b = 0, floor(sqrt(c))
        while a <= b:
            p = a * a + b * b
            if p == c:
                return True
            elif p > c:
                b -= 1
            else:        
                a += 1

        return False        
        