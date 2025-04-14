class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
   
        provinces = 0
        visited_cities = set()

        def dfs(city): 
            visited_cities.add(city)
            for i in range(len(isConnected[city])):
                if isConnected[city][i] == 1:
                    if i not in visited_cities:
                        dfs(i)
        
        for i in range(len(isConnected)):
            if i not in visited_cities:
                provinces += 1
                dfs(i)
        
        return provinces