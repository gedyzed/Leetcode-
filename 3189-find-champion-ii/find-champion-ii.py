class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        degree = defaultdict(int) 
        for a, b in edges:
            degree[b] += 1 

        res = []   
        for num in range(n):
            if not degree[num]:
                res.append(num) 

        return res[0] if len(res) == 1 else -1           

 


     
      
        