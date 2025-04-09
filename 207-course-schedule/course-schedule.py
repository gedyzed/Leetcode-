class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(node):

            if colors[node] == 1:
                return False

            if colors[node] == 2:
                return True  

            colors[node] = 1
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            colors[node] = 2
            return True      
   

        graph = defaultdict(list)
        for course1, course2 in prerequisites:
            graph[course1].append(course2)  

        colors = defaultdict(int)
        for course in range(numCourses):
            if not colors[course]:
                if not dfs(course):
                    return False

        return True     




        