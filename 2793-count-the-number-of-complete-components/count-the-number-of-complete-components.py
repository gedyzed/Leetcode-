class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                self.degree += 1
                nodes.add(nei)
                if nei not in visited:
                    dfs(nei)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        complete = 0
        for i in range(n):
            self.degree = 0 
            nodes = set([i])
            if i not in visited:
                dfs(i)
                n = len(nodes)
                if n * (n - 1) == self.degree:
                    complete += 1

        return complete            






