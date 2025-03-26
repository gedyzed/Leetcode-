class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def validate(k):
            hrs = 0
            for i in range(len(piles)): 
                hrs += ceil(piles[i] / k)
            return hrs <= h
                  

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low   

