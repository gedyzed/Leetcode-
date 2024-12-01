class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        val = sum(cardPoints)
        if k==len(cardPoints):
            return val
        n = len(cardPoints)
        v = sum(cardPoints[:len(cardPoints)-k])
        ret = 0
        ret = max(0, val-v)
        for i in range(n-k, n):
            v += cardPoints[i]
            v -= cardPoints[i-(n-k)]
            ret = max(ret, val-v)

        return ret