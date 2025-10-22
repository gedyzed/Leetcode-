class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        
        def dijkstra(n, start_node):
            distances = {node: float('-inf') for node in range(n)}
            distances[start_node] = -1
            heap = [(-1, start_node)]
            processed = set()

            while heap:
                cur_dist, cur_node = heappop(heap)
                if cur_node in processed:
                    continue
                processed.add(cur_node)
                for nei, weight in graph[cur_node]:
                    new_dist = -cur_dist * weight
                    if new_dist > distances[nei]:
                        distances[nei]= new_dist
                        heappush(heap, (-new_dist, nei))
            
            return distances

        distances = dijkstra(n, start_node)
        ans = distances[end_node]
        return ans if ans != float('-inf') else 0