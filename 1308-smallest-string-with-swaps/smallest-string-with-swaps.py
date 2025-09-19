class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i, j)
        
        idxs = defaultdict(list)
        letters = defaultdict(list)
        for i, char in enumerate(s):
            rt = uf.find(i)
            idxs[rt].append(i)
            letters[rt].append(char)
        
        for ky, val in letters.items():
            letters[ky].sort()

        ans = [""] * len(s)
        for k, idxs_ in idxs.items():
            for i, idx in enumerate(idxs_):
                ans[idx] = letters[k][i]

        return "".join(ans)        

    

class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):

        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
    


        