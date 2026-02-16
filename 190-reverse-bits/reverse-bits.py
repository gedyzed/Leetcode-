class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0
        for i in range(31):
            if n & 1:
                ans |= 1

            n = n >> 1
            ans <<= 1
         
        return ans
        