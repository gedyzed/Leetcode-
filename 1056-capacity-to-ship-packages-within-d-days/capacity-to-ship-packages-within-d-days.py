class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def validate(capacity):
        
            load, day = 0, 1
            for weight in weights:
                if load + weight <= capacity:
                    load += weight
                else:
                    day += 1
                    load = weight

            return day <= days    

        left, right = max(weights), sum(weights)        
        while left <= right:
            mid = (left + right) // 2
            if validate(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left     
                       

        