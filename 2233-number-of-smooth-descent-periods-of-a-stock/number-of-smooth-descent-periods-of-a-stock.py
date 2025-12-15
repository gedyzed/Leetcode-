class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        left, count = 0, 1
        for right in range(1, len(prices)):
            if prices[right - 1] - 1 != prices[right]:
                left = right
            else:
                count += right - left
            count += 1
        
        return count
             
      