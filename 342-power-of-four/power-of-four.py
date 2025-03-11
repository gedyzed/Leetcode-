class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if not n:
            return False

        e = int(math.log(abs(n), 4))
        return n == 4 ** e

        