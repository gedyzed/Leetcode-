class Solution:
    def maximumCandies(self, candies: List[int], childs: int) -> int:

        def validate(k):
            child = 0
            for i in range(len(candies)):
                if k <= candies[i]:
                    child += candies[i] // k

            return child >= childs       

        low, high = 1, max(candies) 
        while low <= high:
            mid = (low + high ) // 2
            if validate(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high            

        