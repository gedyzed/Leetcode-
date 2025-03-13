class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        res = 0
        for people in range(1, n + 1):
            res = (res + k) % people

        return res + 1    

          