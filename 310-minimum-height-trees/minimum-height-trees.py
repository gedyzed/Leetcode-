class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
            

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque()
        edge_count = {} 
        for src, nei in graph.items():
            if len(nei) == 1:
                queue.append(src)
            edge_count[src] = len(nei)

        while queue:
            if n <= 2:
                return list(queue)

            for i in range(len(queue)):
                node = queue.popleft()  
                n -= 1 
                for nei in graph[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        queue.append(nei)             


                

     


           
        