class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        graph = defaultdict(list)
        for i in range(len(original)):
            org, ch = original[i], changed[i]
            c = cost[i]
            graph[org].append((ch, c))

        def dikjsatra(source_node):
            distances = [float('inf')] * 26
            heap = [(0, source_node)]
            idx = ord(source_node) - ord('a')
            distances[idx] = 0
        
            while heap:
                cost_, node = heappop(heap)
                for nei, weight in graph[node]:
                    new_dist = cost_ + weight
                    idx = ord(nei) - ord('a')
                    if new_dist < distances[idx]:
                        distances[idx] = new_dist
                        heappush(heap, (new_dist, nei))
            
            return distances

        ans, added = 0, defaultdict(list)
        for i, src in enumerate(source):
            idx = ord(target[i]) - ord('a')
            if src not in added:
                dist = dikjsatra(src)
                added[src] = dist
            else:
                dist = added[src]
            if dist[idx] == float('inf'):
                return -1

            ans += dist[idx]
           
        return ans       

