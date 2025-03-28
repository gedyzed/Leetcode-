class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
        min_rad = 0

        for house in houses:

            idx = bisect_left(heaters, house)
            left_dist = float("inf") if idx == 0 else abs(house - heaters[idx - 1])
            right_dist = float("inf") if len(heaters) == idx else abs(heaters[idx] - house)

            min_rad = max(min_rad, min(left_dist, right_dist))
        return min_rad
            



        