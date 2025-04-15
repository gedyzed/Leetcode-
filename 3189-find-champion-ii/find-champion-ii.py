class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:


        vert = set() # nodes 
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            vert.add(a)
            vert.add(b)

        counter = defaultdict(int) 
        for a, nodes in adj_list.items():
            counter[a] += 0
            for node in nodes:
                counter[node] += 1

        counts = list(counter.values())
        if counts:
            min_count = min(counts)

        res = []
        for node, cnt in counter.items():
            if cnt == min_count:
                res.append(node)            

        if (len(vert) != n and n > 1) or len(res) > 1:
            return -1
        elif not res and n == 1:
            return 0  
        return res[0]               
             


     
      
        