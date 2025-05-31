class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        un = UnionFind(len(edges) + 1)
        for a, b in edges:
            un.union(a, b)

        return un.ans
     

class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        self.ans = 0
        
    def find(self, X):

        if X == self.root[X]:
            return self.root[X]
        self.root[X] = self.find(self.root[X])
        return self.root[X]


    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)

        if rootX == rootY:
            self.ans = [X, Y]
            return 

        rankX = self.rank[rootX]    
        rankY = self.rank[rootY]

        if rankX > rankY:
            self.root[rootY] = rootX
        elif rankX < rankY:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1      





         