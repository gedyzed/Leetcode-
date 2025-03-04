class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        city = [(a - b, a, b) for a, b in costs]
        city.sort() 
    
        n, ans = len(costs) // 2, 0     
        for i in range(len(city)):
            if i < n:
                ans += city[i][1]
            else:
                ans += city[i][2]  

        return ans          

    
        