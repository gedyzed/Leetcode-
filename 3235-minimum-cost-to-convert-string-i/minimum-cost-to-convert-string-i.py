from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        n = 26
        INF = float('inf')
        
        # Initialize distance matrix
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0  # zero cost to convert a letter to itself
        
        # Add edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)  
        
        # Floyd-Warshall: all-pairs shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Calculate total cost
        total_cost = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]
        
        return total_cost
