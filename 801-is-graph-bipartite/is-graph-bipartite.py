class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = defaultdict(int)
        Red, Blue = 1, 2

        def dfs(node):

            for nei in graph[node]:
                if not colors[nei]:
                    if colors[node] == Blue:
                        colors[nei] = Red
                    else:
                        colors[nei] = Blue

                    if not dfs(nei):
                        return False  

                elif colors[nei] == colors[node]:
                    return False

            return True

        for node in range(len(graph)):
            if not colors[node]:  
                colors[Red] 
                if not dfs(node):
                    return False

        return True            


                         


                        




    
        