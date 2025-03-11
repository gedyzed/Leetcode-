class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        e = math.log(abs(n), 4)
        return e == int(e)

        