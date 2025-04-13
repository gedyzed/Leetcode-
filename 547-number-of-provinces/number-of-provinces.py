class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):

            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)

        adj_list = defaultdict(list)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col]:
                    adj_list[row].append(col) 
                    adj_list[col].append(row)

        visited = set()
        province = 0
        for row in range(len(isConnected)):
            if row not in visited:
                dfs(row)
                province += 1
                
        return province            
                                   
                        
        



        