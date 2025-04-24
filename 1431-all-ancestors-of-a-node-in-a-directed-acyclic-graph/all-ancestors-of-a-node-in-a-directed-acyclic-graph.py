class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            in_degree[b] += 1
        
        queue = deque()   
        for node in range(n):
            if not in_degree[node]:
                queue.append(node)

        res = defaultdict(set)
        while queue:
            node = queue.popleft()  
            for nei in graph[node]:
                res[nei].update(res[node])
                res[nei].add(node)
                in_degree[nei] -= 1
                if not in_degree[nei]:
                    queue.append(nei)

       
        return [sorted(list(res[i])) for i in range(n)]




            
            
