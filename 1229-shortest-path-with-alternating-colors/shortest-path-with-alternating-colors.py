class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:


        def bfs(target, start_with_red):
            
            queue = deque([(0, 0, start_with_red)])
            visited = set((0, start_with_red))
            while queue:
                
                node, lvl, flag = queue.popleft()
                if node == target:
                    return lvl

                if not flag :
                    for nei in red[node]:
                        if (nei, True) not in visited:
                            queue.append((nei, lvl + 1, True))  
                            visited.add((nei, True))
                else:
                    for nei in blue[node]:
                        if (nei, False) not in visited:
                            queue.append((nei, lvl + 1, False))
                            visited.add((nei, False))
                
            return 101     

                    
        red = defaultdict(list)
        blue = defaultdict(list)

        for a, b in redEdges:
            red[a].append(b)

        for u, v in blueEdges:
            blue[u].append(v)  

        ans = []
        for i in range(n):
            x = min(bfs(i, False), bfs(i, True))  
            if x == 101:
                x = -1
            ans.append(x)

        return ans     






           
                        




        

            
                


        