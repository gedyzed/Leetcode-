from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
      
        un = UnionFind(26)
        for eq in equations:
            if eq[1] == '=':          
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                un.union(x, y)

        for eq in equations:
            if eq[1] == '!':          
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
             
                if un.find(x) == un.find(y):
                    return False

        return True


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, X):
        if X == self.root[X]:
            return X
        self.root[X] = self.find(self.root[X])
        return self.root[X]

    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
