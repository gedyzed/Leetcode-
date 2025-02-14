class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints) - k
        sum_ = sum(cardPoints[:n])
        total_sum = sum(cardPoints)
        left, max_sum = 0, total_sum - sum_
        for right in range(n, len(cardPoints)):
            sum_ -= cardPoints[left]
            sum_ += cardPoints[right]
            left += 1
            max_sum = max(max_sum, total_sum - sum_)

        return max_sum    

         
            

      
         