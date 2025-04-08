class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for ngr in graph[node]:
                if ngr not in visited:
                    found = dfs(ngr)    
                    if found:
                        return True

            return False  

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set() 
        return dfs(source)   
  


        