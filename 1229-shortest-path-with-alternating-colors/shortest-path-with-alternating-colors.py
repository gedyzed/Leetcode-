class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
                 
        red = defaultdict(list)
        blue = defaultdict(list)

        for a, b in redEdges:
            red[a].append(b)

        for u, v in blueEdges:
            blue[u].append(v)  

        queue = deque([(0, 0, None)])
        visited = set((0, None))
        ans = [-1 for _ in range(n)]
        while queue:
            
            node, lvl, flag = queue.popleft()
            if ans[node] == -1:
                ans[node] = lvl

         
            if flag != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visited:
                        queue.append((nei, lvl + 1, "RED"))  
                        visited.add((nei, "RED"))

            if flag != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visited:
                        queue.append((nei, lvl + 1, "BLUE"))
                        visited.add((nei, "BLUE"))
                
        return ans     






           
                        




        

            
                


        