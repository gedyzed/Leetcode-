class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        cities = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if x == cities[x]:
                return x

            cities[x] = find(cities[x])   
            return cities[x] 

        def union(x, y):
            rootX, rootY  = find(x), find(y)  
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    cities[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    cities[rootX] = rootY
                else:
                    cities[rootX] = rootY
                    rank[rootY] += 1   
                return True
                
            return False         

        provinces = n
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] :
                        if union(row, col):
                            provinces -= 1

        return provinces



        



   
       