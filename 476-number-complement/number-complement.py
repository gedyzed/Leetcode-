class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        mask = (1 << n) - 1
        return num ^ mask

        