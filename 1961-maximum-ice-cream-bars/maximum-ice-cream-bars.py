class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        max_, min_ = max(costs), min(costs)
        count_array = [0] * (max_ - min_ + 1)

        for cost in costs:
            count_array[cost - min_] += 1

        s_costs = [] 
        for i, count in enumerate(count_array):
            s_costs.extend([i + min_] * count) 

        ice_creams = 0
        for cost in s_costs:
            if cost > coins or coins < cost:
                break

            ice_creams += 1
            coins -= cost

        return ice_creams        



        