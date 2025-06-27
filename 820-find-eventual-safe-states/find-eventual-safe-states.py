class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        graph_modified = defaultdict(list) 
        outgoing = defaultdict(int)
        for i, nei in enumerate(graph):
            for node in nei:
                graph_modified[node].append(i)
                outgoing[i] += 1

        queue = deque()
        for node, nei in enumerate(graph):
            if not nei:
                queue.append(node)

        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in graph_modified[node]:
                outgoing[nei] -= 1
                if not outgoing[nei]:
                    queue.append(nei) 

        return sorted(ans)                   
                 





        