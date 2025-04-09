class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
         
        def dfs(node):

            if colors[node] == GRAY:
                return False

            if colors[node] == BLACK:
                return True  

            colors[node] = GRAY
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            colors[node] = BLACK
            return True      
   

        graph = defaultdict(list)
        for course1, course2 in prerequisites:
            graph[course1].append(course2)  

        colors = defaultdict(int)
        for course in range(numCourses):
            if colors[course] == WHITE:
                if not dfs(course):
                    return False

        return True     




        