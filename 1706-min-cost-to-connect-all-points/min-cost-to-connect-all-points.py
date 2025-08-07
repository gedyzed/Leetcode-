import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

     
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))

  
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, node)
        total_cost = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            total_cost += cost
            for wt, nei in graph[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap, (wt, nei))

        return total_cost