class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        parent = list(range(len(strs)))
        rank = [0] * len(strs)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]    

        def union(x, y):
            root_x, root_y = find(x), find(y)    
            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
  
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                count = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                    
                if count == 2 or count == 0:
                    union(i, j)

        ans = len({find(i) for i in range(len(strs))})
        return ans
        

          


        