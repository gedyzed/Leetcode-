class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def validate(time, cars):

            num_cars = 0
            for rank in ranks: 
                num_cars += int(sqrt(time / rank )) 
            return num_cars >= cars

        left, right = 1, min(ranks) * cars * cars
        while left <= right:
            mid = (left + right ) // 2
            if validate(mid, cars):
                right = mid - 1
            else:
                left = mid + 1

        return left                   

        