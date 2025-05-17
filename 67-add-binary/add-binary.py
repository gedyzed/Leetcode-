class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a, b = int(a, 2), int(b, 2)
        sum = (a | b) + (a & b)
        return bin(sum)[2:]
        