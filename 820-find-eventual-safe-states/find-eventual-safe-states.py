class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        colors = defaultdict(int)
        def dfs(node):

            for nei in graph[node]:
                if colors[nei] == 1:
                    return True

                if colors[nei] == 0: 
                    colors[nei] = 1
                    if dfs(nei):
                        return True

            ans.append(node) 
            colors[node] = 2  
            return False     

        ans = []
        for node in range(len(graph)):
            if not colors[node]:
                colors[node] == 1
                dfs(node)
              

        return sorted(ans)        
                
                
            





                         
                 
       