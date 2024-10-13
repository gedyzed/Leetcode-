class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        return max(self.maxConsecutive(answerKey,k,'T'), self.maxConsecutive(answerKey,k,'F'))

    def maxConsecutive(self,answerKey: str,k: int ,ch: str) -> int:

        left = 0
        n = len(answerKey)
        max_confusion = 0
        change = 0

        for right in range(n):
            if answerKey[right] != ch:
                change += 1

            while change > k : 
                if answerKey[left] != ch:
                    change -= 1
                left += 1
            max_confusion = max(max_confusion,right - left + 1)

        return max_confusion    







        