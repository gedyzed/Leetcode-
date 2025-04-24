class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        outgoing = defaultdict(int)
        graph_ = defaultdict(list)
        for i, nodes in enumerate(graph):
            outgoing[i] += len(nodes)
            for node in nodes:
                graph_[node].append(i)
            
        queue = deque() 
        res = [] 

        for i in range(len(graph)):
            if not outgoing[i]:
                queue.append(i)   

        while queue:
            node = queue.popleft() 
            res.append(node)

            for nei in graph_[node]:
                outgoing[nei] -= 1
                if outgoing[nei] == 0:
                    queue.append(nei)

        return sorted(res)            

           
                




               


        
        