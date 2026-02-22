class Solution:
    def binaryGap(self, n: int) -> int:

        left, ans = -1, 0
        for i in range(32):
            bit = n & 1
            n = n >> 1
            if bit and left == -1:
                left = i
            elif bit:
                ans = max(ans, i - left)
                left = i
        
        return ans
