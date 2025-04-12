class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for u, c in adj.items():
            if len(adj[u]) == len(adj) - 1:
                return u 
        