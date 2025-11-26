class Solution:
    def __init__(self):
        self.directions  = [(0,1),(1,0),(-1,0),(0,-1)]
        self.visted = []
    def bfs(self,i,j,grid):
        q = deque()
        q.append((i,j))
        self.visted[i][j] = 1
        while q:
            x,y = q.popleft()
            for o,p in self.directions:
                newx = x+o
                newy = y+p
                cond = 0<=newx <len(grid) and  0<= newy<len(grid[0])
                if cond and grid[newx][newy]=="1" and self.visted[newx][newy]==0:
                    self.visted[newx][newy] = 1
                    q.append((newx,newy)) 
                                                                      
    def solve(self,grid):
        self.visted = [[0]*len(grid[0]) for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and  self.visted[i][j]==0:
                    self.bfs(i,j,grid)
                    count+=1
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.solve(grid)

        
        