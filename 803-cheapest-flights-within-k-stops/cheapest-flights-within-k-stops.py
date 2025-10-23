class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        distances = {node: float('inf') for node in range(n)}
        distances[src] = 0
        queue = deque([(0, src, 0)])
    
        while queue: 
            dist, node, stops = queue.popleft()
            if stops > k:
                break

            for nei, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    queue.append((new_dist, nei, stops + 1))

        
        ans = distances[dst]  
        if ans == float('inf'):
            return -1             
        return ans 

      