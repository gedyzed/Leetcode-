class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        incoming = defaultdict(int)
        for a, b in richer:
            graph[a].append(b)
            incoming[b] += 1

        queue = deque()
        res = list(range(len(quiet)))

        for i in range(len(quiet)):
            if not incoming[i]:
                queue.append(i)

        while queue:
            node = queue.popleft() 

            for nei in graph[node]:
                if quiet[res[node]] < quiet[res[nei]]:
                    res[nei] = res[node]

                incoming[nei] -= 1
                if not incoming[nei]:
                    queue.append(nei)
     
        return res            

                
                

                   

          
        
        