class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        WHITE, GREEN, BLUE = 0, 1, 2
        def dfs(node):
            
            for neighbour in graph[node]:
                if colors[neighbour] == WHITE:
                    if colors[node] == BLUE:
                        colors[neighbour] = GREEN
                    else:
                        colors[neighbour] = BLUE 

                    if not dfs(neighbour):
                        return False

                elif colors[neighbour] == colors[node]:
                    return False
                    
            return True             
            
        graph = defaultdict(list)   
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)  

        colors = defaultdict(int) 
        for node in range(1, n + 1):
            
            if colors[node] == WHITE:
                colors[node] = GREEN
                if not dfs(node):
                    return False

        return True        


            








