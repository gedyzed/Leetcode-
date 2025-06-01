class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        un = UnionFind(n)
       
        for i in range (n):
            emails = set(accounts[i])
            for j in range(i + 1, n):
                for k in range(1, len(accounts[j])):
                    email = accounts[j][k]
                    if email in emails:
                        un.union(i, j)


        emails = defaultdict(set)
        names = dict()

        for i in range(len(accounts)):
            idx = un.find(i)
            names[idx] = accounts[idx][0]
            emails[idx].update(accounts[i])
            
        ans = []   
        for key in emails:   
            emails[key].remove(names[key]) 
            lst = [names[key]] + sorted(list(emails[key]))
            ans.append(lst)
        
        ans.sort()
        return ans          
                      

class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

        
    def find(self, X):

        if X == self.root[X]:
            return self.root[X]
        self.root[X] = self.find(self.root[X])
        return self.root[X]


    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)

        if rootX == rootY:
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
        


        
        