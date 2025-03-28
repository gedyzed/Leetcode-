class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def validate(r):

            num_h = i = 0
            for house in houses:
                while i < len(heaters) and abs(house - heaters[i]) > r:
                    i += 1

                if i < len(heaters):
                    num_h += 1    
                        
            return num_h >= len(houses)            

        houses, heaters = sorted(houses), sorted(heaters)
        low, high = 0, max(houses[-1], heaters[-1])
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1   

        return low        
        