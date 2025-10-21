class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def disktara(n, start_node, threshold):
            distances = {node: float('inf') for node in range(n)}
            distances[start_node] = 0
            processed = set()
            heap = [(0, start_node)]
            count = 0
            while heap:
                c_dist, cur_node = heappop(heap)
                for nei, weight in graph[cur_node]:
                    new_dist = c_dist + weight
                    if new_dist < distances[nei] and new_dist <= threshold:
                        distances[nei] = new_dist
                        heappush(heap, (new_dist, nei))
                        if nei not in processed:
                            count += 1
                            processed.add(nei)
                      
            return count
        
        ans = count = n
        for node in range(n):
            res = disktara(n, node, distanceThreshold)
            if res <= count:
                ans = node
                count = res
            
        return ans

                    